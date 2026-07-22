from dataclasses import dataclass
from pathlib import Path


@dataclass
class DocumentFile:
    """
    Represents a document discovered in the Knowledge Base.
    """

    path: Path
    championship: str
    section: str