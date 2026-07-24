from dataclasses import dataclass


@dataclass
class DocumentPage:
    championship: str
    section: str
    source: str
    page: int
    text: str