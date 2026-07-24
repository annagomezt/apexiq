from pathlib import Path

from app.models.document import Document


class DocumentLoader:

    def __init__(self, knowledge_base_path: Path | None = None):

        if knowledge_base_path is None:
            knowledge_base_path = (
                Path(__file__).resolve().parents[4]
                / "knowledge_base"
            )

        self.knowledge_base_path = knowledge_base_path

    def load(self, path: Path | None = None) -> list[Document]:

        base = path or self.knowledge_base_path

        documents = []

        for pdf in sorted(base.rglob("*.pdf")):

            relative = pdf.relative_to(base)

            championship = relative.parts[0]
            section = relative.parts[1]

            documents.append(
                Document(
                    path=pdf,
                    championship=championship,
                    section=section,
                )
            )

        return documents