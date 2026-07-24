from app.services.embedding_service import EmbeddingService
from app.vector_store.faiss_store import FaissStore


print("=" * 80)
print("APEXIQ - FAISS TEST")
print("=" * 80)

texts = [
    "The pit lane speed limit is 80 km/h.",
    "Drivers must wear helmets.",
    "The Safety Car may be deployed.",
    "Yellow flags indicate danger.",
    "Parc fermé starts after qualifying."
]

embedding_service = EmbeddingService()

print("\nGenerating embeddings...")

embeddings = embedding_service.embed_batch(texts)

print(f"Generated {len(embeddings)} embeddings.")

dimension = len(embeddings[0])

print(f"Embedding dimension: {dimension}")

store = FaissStore(dimension)

store.add(
    ids=list(range(len(texts))),
    embeddings=embeddings
)

print("\nFAISS index created successfully!")

question = "What is the pit lane speed limit?"

question_embedding = embedding_service.embed(question)

scores, indices = store.search(
    question_embedding,
    k=3
)

print("\nTOP RESULTS")
print("=" * 80)

for score, index in zip(scores, indices):

    print(f"\nScore: {score:.4f}")
    print(texts[index])