from pathlib import Path

from app.services.document_loader import DocumentLoader
from app.pipeline.document_pipeline import DocumentPipeline
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStore


class IndexBuilder:

    def __init__(self):

        self.loader = DocumentLoader()
        self.pipeline = DocumentPipeline()
        self.embedding_service = EmbeddingService()

    def build(
        self,
        knowledge_base: Path,
        output_directory: Path,
    ):

        print("=" * 80)
        print("APEXIQ INDEX BUILDER")
        print("=" * 80)

        documents = self.loader.load(knowledge_base)

        print(f"\nDocuments found: {len(documents)}\n")

        store = None

        total_regulations = 0
        total_chunks = 0

        for document in documents:

            print(f"Processing: {document.path.name}")

            _, regulations, chunks = self.pipeline.process(
                pdf_path=document.path,
                championship=document.championship,
                section=document.section,
            )

            total_regulations += len(regulations)
            total_chunks += len(chunks)

            for chunk in chunks:

                embedding = self.embedding_service.embed(chunk.text)

                if store is None:
                    store = VectorStore(
                        dimension=len(embedding)
                    )

                store.add(
                    embedding=embedding,
                    metadata=chunk.model_dump()
                )

            print(f"   Regulations: {len(regulations)}")
            print(f"   Chunks.....: {len(chunks)}\n")

        print("=" * 80)
        print("Saving index...")
        print("=" * 80)

        store.save(output_directory)

        print("\nDone!\n")

        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)

        print(f"Documents   : {len(documents)}")
        print(f"Regulations : {total_regulations}")
        print(f"Chunks      : {total_chunks}")
        print(f"Vectors     : {len(store.metadata)}")