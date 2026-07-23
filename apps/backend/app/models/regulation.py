from pydantic import BaseModel


class Regulation(BaseModel):
    championship: str

    section: str

    regulation_id: str

    title: str

    page: int

    text: str