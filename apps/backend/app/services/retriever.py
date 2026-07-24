from pathlib import Path

from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedding = EmbeddingService()

        self.store = None

    def load(self, directory: Path):

        self.store = VectorStore.load(directory)

    def search(
        self,
        question: str,
        top_k: int = 5,
    ):

        embedding = self.embedding.embed(question)

        return self.store.search(
            embedding,
            k=top_k,
        )