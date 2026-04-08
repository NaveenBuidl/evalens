from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import yaml
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    corpus_path: str
    chunk_size: int
    chunk_overlap: int
    retrieval_k: int
    model: str
    embedding_model: str
    chroma_path: str
    collection_name: str
    groq_api_key: str


def load_settings(config_path: str = "config.yaml") -> Settings:
    cfg_file = Path(config_path)
    if not cfg_file.exists():
        raise FileNotFoundError(f"Missing config file: {cfg_file}")

    with cfg_file.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    groq_api_key = os.getenv("GROQ_API_KEY", "")

    return Settings(
        corpus_path=cfg.get("corpus_path", "D:/Evalens/corpus/intercom_external/raw_pdfs"),
        chunk_size=int(cfg.get("chunk_size", 1000)),
        chunk_overlap=int(cfg.get("chunk_overlap", 150)),
        retrieval_k=int(cfg.get("retrieval_k", 4)),
        model=cfg.get("model", "llama-3.1-8b-instant"),
        embedding_model=cfg.get("embedding_model", "sentence-transformers/all-MiniLM-L6-v2"),
        chroma_path=cfg.get("chroma_path", ".chroma"),
        collection_name=cfg.get("collection_name", "intercom_pdfs"),
        groq_api_key=groq_api_key,
    )
