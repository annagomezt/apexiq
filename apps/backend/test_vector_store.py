from pathlib import Path

from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


embedding_service = EmbeddingService()

texts = [
    "The pit lane speed limit is 80 km/h.",
    "Drivers must wear helmets.",
    "The Safety Car may be deployed.",
    "Formula One has 24 races.",
    "Yellow flags indicate danger."
]

print("=" * 80)
print("VECTOR STORE TEST")
print("=" * 80)

vectors = [
    embedding_service.embed(text)
    for text in texts
]

store = VectorStore(
    dimension=len(vectors[0])
)

for text, vector in zip(texts, vectors):

    store.add(
        embedding=vector,
        metadata={
            "text": text
        }
    )

query = "What is the speed limit in the pit lane?"

query_embedding = embedding_service.embed(query)

results = store.search(
    query_embedding,
    k=3
)

print()

for result in results:

    print(result["distance"])
    print(result["metadata"]["text"])
    print()