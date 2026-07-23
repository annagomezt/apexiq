from pathlib import Path

from app.parsers.pdf_parser import PDFParser
from app.services.regulation_extractor import RegulationExtractor
from app.services.chunk_service import ChunkService


class DocumentPipeline:

    def __init__(self):

        self.parser = PDFParser()

        self.extractor = RegulationExtractor()

        self.chunker = ChunkService()

    def process(
        self,
        pdf_path: Path,
        championship: str,
        section: str,
    ):

        pages = self.parser.parse(
            pdf_path=pdf_path,
            championship=championship,
            section=section,
        )

        regulations = self.extractor.extract(pages)

        chunks = self.chunker.chunk(regulations)

        return pages, regulations, chunks