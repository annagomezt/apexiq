from pathlib import Path
import re

from app.parsers.pdf_parser import PDFParser
from app.models.document_analysis import DocumentAnalysis


class DocumentAnalyzer:

    def __init__(self):
        self.parser = PDFParser()

    def analyze(
        self,
        pdf_path: Path,
        championship: str,
        section: str
    ) -> DocumentAnalysis:

        pages = self.parser.parse(
            pdf_path=pdf_path,
            championship=championship,
            section=section
        )

        article_pattern = re.compile(
            r"ARTICLE\s+\d+",
            re.IGNORECASE
        )

        chapter_pattern = re.compile(
            r"CHAPTER\s+\d+",
            re.IGNORECASE
        )

        appendix_pattern = re.compile(
            r"APPENDIX",
            re.IGNORECASE
        )

        articles = []
        chapters = []
        appendices = []

        empty_pages = []

        total_characters = 0

        for page in pages:

            text = page.text

            total_characters += len(text)

            if not text.strip():
                empty_pages.append(page.page)

            articles.extend(article_pattern.findall(text))
            chapters.extend(chapter_pattern.findall(text))
            appendices.extend(appendix_pattern.findall(text))

        analysis = DocumentAnalysis(
            source=pdf_path.name,
            pages=len(pages),
            characters=total_characters,
            articles=sorted(set(articles)),
            chapters=sorted(set(chapters)),
            appendices=len(appendices),
            empty_pages=empty_pages
        )

        return analysis

    @staticmethod
    def print_report(analysis: DocumentAnalysis):

        print("\n" + "=" * 70)
        print("DOCUMENT ANALYSIS")
        print("=" * 70)

        print(f"Source.............: {analysis.source}")
        print(f"Pages..............: {analysis.pages}")
        print(f"Characters.........: {analysis.characters}")
        print(f"Articles...........: {len(analysis.articles)}")
        print(f"Chapters...........: {len(analysis.chapters)}")
        print(f"Appendices.........: {analysis.appendices}")
        print(f"Empty Pages........: {len(analysis.empty_pages)}")

        if analysis.empty_pages:
            print(f"Pages: {analysis.empty_pages}")

        print("\nArticles Found")

        for article in analysis.articles:
            print(f" • {article}")

        print("=" * 70)


if __name__ == "__main__":

    analyzer = DocumentAnalyzer()

    analysis = analyzer.analyze(
        pdf_path=Path(
            "knowledge_base/formula1/sporting/section_b_sporting.pdf"
        ),
        championship="formula1",
        section="sporting"
    )

    analyzer.print_report(analysis)