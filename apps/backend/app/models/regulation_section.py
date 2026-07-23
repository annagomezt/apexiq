from pydantic import BaseModel


class RegulationSection(BaseModel):
    """
    Represents a logical section extracted from a regulation document.
    """

    championship: str
    section: str

    source: str
    page: int

    article: str
    title: str | None = None

    text: str