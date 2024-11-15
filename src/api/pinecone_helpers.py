from pinecone import Pinecone, QueryResponse, Index

from src.api.settings import settings
from src.api.vectorize import SentenceVectorizator


class PineconeHandle:

    def __init__(self) -> None:
        self.pc: Pinecone = Pinecone(api_key=settings.pinecone_api_key)
        self.vectorizator: SentenceVectorizator = SentenceVectorizator()

    def search(
        self,
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
