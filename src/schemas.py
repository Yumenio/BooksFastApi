from pydantic import BaseModel

class BookRequest(BaseModel):
    name: str