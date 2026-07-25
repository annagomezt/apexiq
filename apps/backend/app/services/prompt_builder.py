class PromptBuilder:

    def build(
        self,
        question: str,
        contexts: list[dict],
    ) -> str:

        context_text = ""

        for i, chunk in enumerate(contexts, start=1):

            metadata = chunk["metadata"]

            context_text += (
                f"\nDOCUMENT {i}\n"
                f"Regulation: {metadata['regulation_id']}\n"
                f"Page: {metadata['page']}\n"
                f"Text:\n"
                f"{metadata['text']}\n"
            )

        prompt = f"""
You are ApexIQ, an AI assistant specialized in motorsport regulations.

Answer ONLY using the provided documents.

If the answer is not present, say:

"I could not find this information in the available regulations."

Always cite the regulation ID and page number.

==============================
DOCUMENTS
==============================

{context_text}

==============================
QUESTION
==============================

{question}

==============================
ANSWER
==============================
"""

        return prompt.strip()