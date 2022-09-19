from pydantic import BaseModel
from datetime import datetime


class BookRequestCreate(BaseModel):
    name: str
    author: str
    price: float
    availability: int

class BookRequest(BaseModel):
    id: int
    name: str
    author: str
    price: float
    availability: int

    class Config:
        orm_mode = True