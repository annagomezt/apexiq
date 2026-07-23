from app.services.document_loader import DocumentLoader
from apps.backend.app.parsers.pdf_parser import PDFParser

loader = DocumentLoader("../../knowledge_base")
parser = PDFParser()

documents = loader.discover_documents()

for document in documents:

    pages = parser.parse(
        document.path,
        document.championship,
        document.section,
    )

    print("=" * 80)
    print(document.path.name)
    print(f"Championship: {document.championship}")
    print(f"Section: {document.section}")
    print(f"Pages: {len(pages)}")

    if pages:
        print("\nFirst page preview:\n")
        print(pages[0].text[:500])