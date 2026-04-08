from __future__ import annotations

from pathlib import Path
from typing import Any

import chromadb
from chromadb.config import Settings as ChromaSettings
from chromadb.utils import embedding_functions
from groq import Groq
import fitz

from app.config import Settings


class RAGEngine:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._chroma = chromadb.PersistentClient(
            path=settings.chroma_path,
            settings=ChromaSettings(allow_reset=False),
        )
        self._embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=settings.embedding_model,
        )
        self._collection = self._chroma.get_or_create_collection(
            name=settings.collection_name,
            embedding_function=self._embedding_fn,
            metadata={"hnsw:space": "cosine"},
        )

        self._groq = Groq(api_key=settings.groq_api_key) if settings.groq_api_key else None

    @staticmethod
    def _chunk_text(text: str, chunk_size: int, chunk_overlap: int) -> list[str]:
        text = " ".join(text.split())
        if not text:
            return []

        chunks: list[str] = []
        start = 0
        step = max(chunk_size - chunk_overlap, 1)
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start += step
        return chunks

    def ingest(self) -> dict[str, Any]:
        corpus = Path(self.settings.corpus_path)
        if not corpus.exists():
            raise FileNotFoundError(f"Corpus folder not found: {corpus}")

        supported_suffixes = {".pdf", ".md", ".txt"}
        source_paths = sorted(
            path for path in corpus.iterdir() if path.is_file() and path.suffix.lower() in supported_suffixes
        )
        if not source_paths:
            return {"indexed_files": 0, "indexed_chunks": 0}

        existing_count = self._collection.count()
        if existing_count > 0:
            return {"indexed_files": 0, "indexed_chunks": existing_count, "skipped": True}

        ids: list[str] = []
        docs: list[str] = []
        metas: list[dict[str, Any]] = []

        for source_path in source_paths:
            if source_path.suffix.lower() == ".pdf":
                with fitz.open(source_path) as pdf_doc:
                    full_text = "\n".join(page.get_text("text") for page in pdf_doc)
            else:
                full_text = source_path.read_text(encoding="utf-8")

            chunks = self._chunk_text(
                full_text,
                self.settings.chunk_size,
                self.settings.chunk_overlap,
            )
            for idx, chunk in enumerate(chunks):
                ids.append(f"{source_path.stem}-{idx}")
                docs.append(chunk)
                metas.append({"source": str(source_path), "chunk_index": idx})

        if ids:
            self._collection.add(ids=ids, documents=docs, metadatas=metas)

        return {"indexed_files": len(source_paths), "indexed_chunks": len(ids), "skipped": False}

    def query(self, user_query: str) -> dict[str, Any]:
        if not user_query.strip():
            raise ValueError("query cannot be empty")

        results = self._collection.query(
            query_texts=[user_query],
            n_results=self.settings.retrieval_k,
            include=["documents", "metadatas", "distances"],
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        chunks = []
        sources = []
        for doc, meta in zip(documents, metadatas):
            source = (meta or {}).get("source", "")
            chunks.append(doc)
            if source and source not in sources:
                sources.append(source)

        answer = self._generate_answer(user_query, chunks)

        return {
            "query": user_query,
            "answer": answer,
            "retrieved_chunks": chunks,
            "sources": sources,
            "model": self.settings.model,
            "retrieval_k": self.settings.retrieval_k,
            "chunk_size": self.settings.chunk_size,
        }

    def _generate_answer(self, query: str, chunks: list[str]) -> str:
        if not chunks:
            return "I couldn't find relevant context in the indexed PDF corpus."

        context = "\n\n".join(chunks[: self.settings.retrieval_k])

        if not self._groq:
            return "Set GROQ_API_KEY to enable generation. Retrieved context is available in retrieved_chunks."

        system = (
            "You answer questions using only the provided context. "
            "If context is insufficient, say so briefly."
        )
        user = f"Context:\n{context}\n\nQuestion: {query}"

        completion = self._groq.chat.completions.create(
            model=self.settings.model,
            temperature=0,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return completion.choices[0].message.content or ""
