from pathlib import Path

from app.services.prompt_builder import PromptBuilder
from app.services.retriever import Retriever
from app.services.llm_service import LLMService


class AIEngine:

    def __init__(self):

        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMService()

        self.retriever.load(Path("data"))

    def ask(self, question: str):

        contexts = self.retriever.search(
            question,
            top_k=5,
        )

        prompt = self.prompt_builder.build(
            question=question,
            contexts=contexts,
        )

        answer = self.llm.generate(prompt)

        return {
            "question": question,
            "answer": answer,
            "sources": contexts,
        }