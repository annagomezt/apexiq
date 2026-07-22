from pathlib import Path

from app.models.document_file import DocumentFile


class DocumentLoader:

    def __init__(self, knowledge_base_path: str):
        self.knowledge_base = Path(knowledge_base_path)

    def discover_documents(self) -> list[DocumentFile]:

        documents = []

        for pdf in self.knowledge_base.rglob("*.pdf"):

            documents.append(
                DocumentFile(
                    path=pdf,
                    championship=pdf.parent.parent.name,
                    section=pdf.parent.name,
                )
            )

        return documents