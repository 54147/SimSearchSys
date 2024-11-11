
from pinecone import Pinecone, QueryResponse, Index
from sentence_transformers import SentenceTransformer

from src.api.settings import settings


def get_pinecone_client():
    return PineconeHandle()


class SentenceVectorizator:
    def __init__(self, model_name_or_path:str = settings.transformers_sentence_model_name) -> None:
        self.model: SentenceTransformer = SentenceTransformer(model_name_or_path)

    def vectorize_query(self, query: str) -> list[float]:
        return [float(t) for t in self.model.encode(query)]


class PineconeHandle:

    def __init__(self) -> None:
        self.pc: Pinecone = Pinecone(api_key=settings.pinecone_api_key)
        self.vectorizator: SentenceVectorizator = SentenceVectorizator()

    def search(self,
               query: str,
               index_name: str = settings.pinecone_index_name, 
               top_k: int = settings.return_k_amount,
               ) -> QueryResponse:

        vector_to_query: list[float] = self.vectorizator.vectorize_query(query)

        current_index: Index = self.pc.Index(index_name)
        return current_index.query(
            vector=vector_to_query,
            top_k=top_k,
            include_metadata=True,
        )

