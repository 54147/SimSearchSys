import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.api.pinecone_helpers import get_pinecone_client


app = FastAPI()
pc_handle = get_pinecone_client()

class SearchResponse(BaseModel):
    id: str
    text: str
    score: float

@app.get("/search")
async def search(query: str, top_k: int = 3):
    try:
        results = pc_handle.search(query, top_k=top_k)

        return {"results": [
            SearchResponse(id=result["id"], 
                           text=result["metadata"]["text"],
                           score=result["score"],)
        for result in results["matches"]]}
    except Exception as e:
        logging.error(f"Error searching in Pinecone: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


           






