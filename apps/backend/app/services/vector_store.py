from pathlib import Path
import pickle

import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension: int):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(dimension)

        self.metadata = []

    def add(self, embedding, metadata):

        vector = np.array([embedding], dtype="float32")

        self.index.add(vector)

        self.metadata.append(metadata)

    def search(self, embedding, k=5):

        vector = np.array([embedding], dtype="float32")

        distances, indices = self.index.search(vector, k)

        results = []

        for distance, index in zip(distances[0], indices[0]):

            if index == -1:
                continue

            results.append(
                {
                    "distance": float(distance),
                    "metadata": self.metadata[index],
                }
            )

        return results

    def save(self, folder: Path):

        folder.mkdir(parents=True, exist_ok=True)

        faiss.write_index(
            self.index,
            str(folder / "index.faiss")
        )

        with open(folder / "metadata.pkl", "wb") as f:
            pickle.dump(self.metadata, f)

    @classmethod
    def load(cls, folder: Path):

        index = faiss.read_index(
            str(folder / "index.faiss")
        )

        with open(folder / "metadata.pkl", "rb") as f:
            metadata = pickle.load(f)

        store = cls(index.d)

        store.index = index

        store.metadata = metadata

        return store