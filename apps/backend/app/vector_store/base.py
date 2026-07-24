from abc import ABC, abstractmethod


class BaseVectorStore(ABC):

    @abstractmethod
    def add(self, ids, embeddings):
        pass

    @abstractmethod
    def search(self, embedding, k=5):
        pass

    @abstractmethod
    def save(self, path):
        pass

    @abstractmethod
    def load(self, path):
        pass