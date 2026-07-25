from app.services.llm_service import LLMService


print("=" * 80)
print("APEXIQ LLM TEST")
print("=" * 80)

llm = LLMService()

response = llm.generate(
    "Say only: ApexIQ connected successfully."
)

print("\nResponse:\n")
print(response)