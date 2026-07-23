from pydantic import BaseModel


class DocumentChunk(BaseModel):
    championship: str

    section: str

    regulation_id: str

    title: str

    source: str

    page: int

    chunk_index: int

    text: str