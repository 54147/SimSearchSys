import logging

from fastapi import FastAPI, HTTPException

from src.api.main_helpers import search_similar_sentences


app = FastAPI()


@app.get("/search")
async def search(query: str, top_k: int = 3):
    try:
        return search_similar_sentences(query, top_k)
    except Exception as e:
        logging.error(f"Error searching in Pinecone: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


           






