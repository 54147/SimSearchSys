import logging

from pydantic import BaseModel

from src.api.pinecone_helpers import PineconeHandle


pc_handle = PineconeHandle()

class SearchResponse(BaseModel):
    id: str
    text: str
    score: float
    
def search_similar_sentences(query_text: str, top_k: int):
    try:
        results = pc_handle.search(query_text, top_k=top_k)

        return {"results": [
            SearchResponse(id=result["id"], 
                           text=result["metadata"]["text"],
                           score=result["score"],)
        for result in results["matches"]]}
    except Exception as e:
        logging.error(f"Failed to search for similar sentences. Error: {e}")
        raise

