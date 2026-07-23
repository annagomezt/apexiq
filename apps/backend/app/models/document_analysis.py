from pydantic import BaseModel


class DocumentAnalysis(BaseModel):

    source: str

    pages: int

    characters: int

    articles: list[str]

    chapters: list[str]

    appendices: int

    empty_pages: list[int]