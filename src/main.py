from fastapi import FastAPI, status, HTTPException
from src.schemas import BookRequest

from .db import Base, engine, Book

from pydantic import BaseModel
from sqlalchemy.orm import Session


Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def root():
    return {"msg" : "Hello World"}

@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookRequest):
    session = Session(bind=engine, expire_on_commit=False)

    new_book = Book(
        name = book.name
    )
    session.add(new_book)
    session.commit()

    id = new_book.id

    session.close()


    return "created new book"

@app.get("/books/{id}")
def read_book(id):
    session = Session(bind=engine, expire_on_commit=False)

    book = session.query(Book).get(id)
    session.close()
    
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    
    return book
    # return {"book_id":book.id, "book_name": book.name}

@app.put("/books/{id}")
def update_book(id):
    return "update"

@app.delete("/books/{id}")
def delete_book(id):
    return "delete"

@app.get("/books")
def read_books_list():
    return "read list"

