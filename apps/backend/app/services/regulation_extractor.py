import re

from app.models.document_page import DocumentPage
from app.models.regulation import Regulation


class RegulationExtractor:

    REGULATION_PATTERN = re.compile(
        r"^(B\d+(?:\.\d+)*)\s*$"
    )

    def extract(self, pages: list[DocumentPage]) -> list[Regulation]:

        regulations = []

        current = None

        started = False

        for page in pages:

            lines = page.text.splitlines()

            i = 0

            while i < len(lines):

                line = lines[i].strip()

                # Ignora páginas vazias
                if not line:
                    i += 1
                    continue

                # Espera encontrar o início real do regulamento
                if not started:

                    if line == "ARTICLE B1: ORGANISATION OF A COMPETITION":
                        started = True

                    i += 1
                    continue

                # Novo regulamento
                if self.REGULATION_PATTERN.fullmatch(line):

                    if current is not None:
                        regulations.append(
                            Regulation(**current)
                        )

                    title = ""

                    if i + 1 < len(lines):

                        candidate = lines[i + 1].strip()

                        if (
                            candidate
                            and not self.REGULATION_PATTERN.fullmatch(candidate)
                        ):
                            title = candidate

                    current = {
                        "championship": page.championship,
                        "section": page.section,
                        "regulation_id": line,
                        "title": title,
                        "page": page.page,
                        "text": "",
                    }

                    i += 1
                    continue

                if current is not None:
                    current["text"] += line + "\n"

                i += 1

        if current is not None:
            regulations.append(
                Regulation(**current)
            )

        return regulations