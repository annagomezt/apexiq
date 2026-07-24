import faiss
import numpy as np

from app.vector_store.base import BaseVectorStore


class FaissStore(BaseVectorStore):

    def __init__(self, dimension: int):

        self.dimension = dimension

        self.index = faiss.IndexFlatIP(dimension)

        self.ids = []

    def add(self, ids, embeddings):

        vectors = np.array(
            embeddings,
            dtype=np.float32
        )

        self.index.add(vectors)

        self.ids.extend(ids)

    def search(
        self,
        embedding,
        k=5
    ):

        vector = np.array(
            [embedding],
            dtype=np.float32
        )

        scores, indices = self.index.search(
            vector,
            k
        )

        return scores[0], indices[0]

    def save(self, path):

        faiss.write_index(
            self.index,
            str(path)
        )

    def load(self, path):

        self.index = faiss.read_index(
            str(path)
        )