import logging
from pathlib import Path

import fitz

from app.models.document import DocumentPage

logger = logging.getLogger(__name__)


class PDFParser:

    def parse(
        self,
        pdf_path: Path,
        championship: str,
        section: str,
    ) -> list[DocumentPage]:

        pages = []

        try:

            document = fitz.open(pdf_path)

            for page_number, page in enumerate(document, start=1):

                try:

                    text = page.get_text().strip()

                    pages.append(
                        DocumentPage(
                            championship=championship,
                            section=section,
                            source=pdf_path.name,
                            page=page_number,
                            text=text,
                        )
                    )

                except Exception as error:

                    logger.warning(
                        f"Could not read page {page_number} from {pdf_path.name}: {error}"
                    )

            document.close()

        except Exception as error:

            logger.error(f"Could not open {pdf_path.name}: {error}")

        return pages