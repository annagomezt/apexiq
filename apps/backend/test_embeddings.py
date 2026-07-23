from app.services.embedding_service import EmbeddingService

service = EmbeddingService()

text = """
Pit lane speed limit is 80 km/h during the competition.
"""

embedding = service.embed(text)

print("=" * 80)
print("Embedding generated successfully!")
print("=" * 80)

print(f"Vector size: {len(embedding)}")

print("\nFirst 10 values:")

for value in embedding[:10]:
    print(value)