from pathlib import Path

from app.pipeline.document_pipeline import DocumentPipeline


ROOT = Path(__file__).resolve().parents[2]

PDF_PATH = (
    ROOT
    / "knowledge_base"
    / "formula1"
    / "sporting"
    / "section_b_sporting.pdf"
)


def separator(title: str):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def main():

    separator("APEXIQ DOCUMENT PIPELINE")

    print(f"PDF: {PDF_PATH}")

    pipeline = DocumentPipeline()

    pages, regulations, chunks = pipeline.process(
        pdf_path=PDF_PATH,
        championship="formula1",
        section="sporting",
    )

    separator("SUMMARY")

    print(f"Pages        : {len(pages)}")
    print(f"Regulations  : {len(regulations)}")
    print(f"Chunks       : {len(chunks)}")

    separator("FIRST REGULATIONS")

    for regulation in regulations[:5]:

        print(f"\nID: {regulation.regulation_id}")
        print(f"Title: {regulation.title}")
        print(f"Page: {regulation.page}")

        preview = regulation.text.replace("\n", " ")

        print(preview[:250])

    separator("FIRST CHUNK")

    if chunks:

        chunk = chunks[0]

        print(f"Championship : {chunk.championship}")
        print(f"Section      : {chunk.section}")
        print(f"Regulation   : {chunk.regulation_id}")
        print(f"Chunk Index  : {chunk.chunk_index}")
        print(f"Page         : {chunk.page}")

        print("\nText:\n")
        print(chunk.text[:1000])

    separator("PIPELINE FINISHED")


if __name__ == "__main__":
    main()