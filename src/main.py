from urllib import response
from fastapi import FastAPI, status, HTTPException, Depends
from src.schemas import BookRequest, BookRequestCreate
from sqlalchemy.orm import class_mapper
from .db import Base, engine, Book, LocalSession

from pydantic import BaseModel
from typing import List

Base.metadata.create_all(engine)

app = FastAPI()

def get_session():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def root():
    return {"mssg" : "hello world"}


@app.post("/books", response_model=BookRequest, status_code=status.HTTP_201_CREATED)
def create_book(book: BookRequestCreate, session = Depends(get_session)):
    print('breakpoint')
    new_book = Book(
        name = book.name,
        author = book.author,
        price = book.price,
        availability = book.availability
        # year_published = book.year_published
    )
    session.add(new_book)
    session.commit()
    session.refresh(new_book)

    return new_book

@app.get("/books/{id}", response_model=BookRequest)
def read_book(id, session = Depends(get_session)):
    book = session.query(Book).get(id)
    
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    
    return book
    # return {"book_id":book.id, "book_name": book.name}

@app.get("/books", response_model=List[BookRequest])
def read_books_list(session = Depends(get_session)):
    book_list = session.query(Book).all()

    return book_list

@app.put("/books/{id}")
def update_book(id, name: str, author: str, price: float, availability: int, session = Depends(get_session)):
    book = session.query(Book).get(id)
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')

    book.name = name
    book.author = author
    book.price = price
    book.availability = availability
    session.commit()

    return book

@app.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id, session = Depends(get_session)):
    book = session.query(Book).get(id)
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
        
    session.delete(book)
    session.commit()

    return None
