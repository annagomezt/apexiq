from pathlib import Path

from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


print("=" * 80)
print("APEXIQ RETRIEVAL TEST")
print("=" * 80)

# ----------------------------------------------------
# Load services
# ----------------------------------------------------

embedding = EmbeddingService()

vector_store = VectorStore.load(
    Path("data")
)

# ----------------------------------------------------
# Question
# ----------------------------------------------------

question = "What is the pit lane speed limit?"

print(f"\nQuestion:\n{question}")

query_vector = embedding.embed(question)

# ----------------------------------------------------
# Search
# ----------------------------------------------------

results = vector_store.search(
    query_vector,
    k=5
)

print("\n")
print("=" * 80)
print("TOP RESULTS")
print("=" * 80)

for i, result in enumerate(results, start=1):

    metadata = result["metadata"]

    print(f"\n#{i}")
    print(f"Distance : {result['distance']:.4f}")

    print("\nMetadata:")

    for key, value in metadata.items():
        print(f"{key:15}: {value}")