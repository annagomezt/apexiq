from pathlib import Path

from app.services.prompt_builder import PromptBuilder
from app.services.retriever import Retriever
from app.services.llm_service import LLMService


class AIEngine:

    def __init__(self):

        print("========== AIEngine ==========")

        print("1 - Creating Retriever...")
        self.retriever = Retriever()
        print("✓ Retriever created")

        print("2 - Creating PromptBuilder...")
        self.prompt_builder = PromptBuilder()
        print("✓ PromptBuilder created")

        print("3 - Creating LLMService...")
        self.llm = LLMService()
        print("✓ LLMService created")

        print("4 - Loading FAISS index...")
        self.retriever.load(Path("data"))
        print("✓ FAISS loaded")

        print("========== AIEngine Ready ==========")

    def ask(self, question: str):

        contexts = self.retriever.search(
            question,
            top_k=5,
        )

        prompt = self.prompt_builder.build(
            question=question,
            documents=contexts,
        )

        answer = self.llm.generate(prompt)

        return {
            "question": question,
            "answer": answer,
            "sources": contexts,
        }