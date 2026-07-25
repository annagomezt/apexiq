from app.services.ai_engine import AIEngine

print("=" * 80)
print("APEXIQ AI ENGINE")
print("=" * 80)

engine = AIEngine()

question = "What is the pit lane speed limit?"

response = engine.ask(question)

print("\nQUESTION\n")
print(response["question"])

print("\nANSWER\n")
print(response["answer"])

print("\nSOURCES\n")

for source in response["sources"]:

    metadata = source["metadata"]

    print(
        f'- {metadata["regulation_id"]} '
        f'(page {metadata["page"]})'
    )