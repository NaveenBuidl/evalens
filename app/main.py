from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.config import load_settings
from app.rag import RAGEngine

settings = load_settings()
rag = RAGEngine(settings)

app = FastAPI(title="Evalens Tracer-Bullet RAG")


class QueryRequest(BaseModel):
    query: str


@app.on_event("startup")
def startup_event() -> None:
    rag.ingest()


@app.post("/query")
def query_api(payload: QueryRequest):
    try:
        return rag.query(payload.query)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except Exception as e:  # minimal tracer-bullet error handling
        raise HTTPException(status_code=500, detail=str(e)) from e
