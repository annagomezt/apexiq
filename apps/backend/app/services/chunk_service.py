from app.models.chunk import DocumentChunk
from app.models.regulation import Regulation


class ChunkService:

    def __init__(self, chunk_size: int = 1200):
        self.chunk_size = chunk_size

    def chunk(
        self,
        regulations: list[Regulation]
    ) -> list[DocumentChunk]:

        chunks = []

        for regulation in regulations:

            text = regulation.text.strip()

            if not text:
                continue

            chunk_index = 1

            for start in range(0, len(text), self.chunk_size):

                end = start + self.chunk_size

                chunks.append(
                    DocumentChunk(
                        championship=regulation.championship,
                        section=regulation.section,
                        regulation_id=regulation.regulation_id,
                        title=regulation.title,
                        source="FIA",
                        page=regulation.page,
                        chunk_index=chunk_index,
                        text=text[start:end],
                    )
                )

                chunk_index += 1

        return chunks