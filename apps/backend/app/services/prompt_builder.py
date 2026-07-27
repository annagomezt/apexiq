class PromptBuilder:

    def build(self, question: str, documents: list):

        context = ""

        for doc in documents:

            metadata = doc["metadata"]

            context += (
                f"""
Regulation ID: {metadata["regulation_id"]}
Title: {metadata["title"]}
Page: {metadata["page"]}

{metadata["text"]}

-------------------------

"""
            )

        prompt = f"""
You are ApexIQ, an AI assistant specialized in FIA Formula 1 regulations.

Your task is to answer ONLY using the regulations provided below.

Rules:

- Reply in the SAME LANGUAGE used by the user.
- Never invent regulations.
- Never make assumptions.
- If the answer is not present in the context, clearly say that you do not have enough information.
- Keep regulation IDs exactly as written.
- Keep article references exactly as written.
- Be concise, clear and professional.
- When possible, mention the regulation ID and page used.

=========================
CONTEXT
=========================

{context}

=========================
QUESTION
=========================

{question}
"""

        return prompt