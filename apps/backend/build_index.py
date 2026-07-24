from pathlib import Path

from app.services.index_builder import IndexBuilder


builder = IndexBuilder()

builder.build(
    knowledge_base=Path("../../knowledge_base"),
    output_directory=Path("data")
)