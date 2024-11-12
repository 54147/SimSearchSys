from sentence_transformers import SentenceTransformer

from src.api.settings import settings


class SentenceVectorizator:
    def __init__(
        self, model_name_or_path: str = settings.transformers_sentence_model_name
    ) -> None:
        self.model: SentenceTransformer = SentenceTransformer(model_name_or_path)

    def vectorize_query(self, query: str) -> list[float]:
        return [float(t) for t in self.model.encode(query)]
