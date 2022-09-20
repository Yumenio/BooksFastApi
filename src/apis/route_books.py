from fastapi import APIRouter, status, HTTPException, Depends
from ..schemas import BookRequest, BookRequestCreate
from ..models.books import Book
from ..db import get_db
from pydantic import BaseModel
from typing import List



router = APIRouter()

# @router.get("/")
# def root():
#     return {"msg" : "Hello World"}


@router.post("/create", response_model=BookRequest, status_code=status.HTTP_201_CREATED)
def create_book(book: BookRequestCreate, session = Depends(get_db)):
    new_book = Book(
        name = book.name,
        author = book.author,
        year = book.year,
        price = book.price,
        availability = book.availability
    )
    session.add(new_book)
    session.commit()
    session.refresh(new_book)

    return new_book


@router.get("/{id}", response_model=BookRequest)
def read_book(id, session = Depends(get_db)):
    book = session.query(Book).get(id)
    
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    
    return book
    # return {"book_id":book.id, "book_name": book.name}

@router.get("/", response_model=List[BookRequest])
def read_books_list(session = Depends(get_db)):
    book_list = session.query(Book).all()

    return book_list

@router.put("/{id}")
# def update_book(id, name: str, author: str, year: int, price: float, availability: int, session = Depends(get_db)):
def update_book(id, book: BookRequestCreate, session = Depends(get_db)):
    dbook = session.query(Book).get(id)
    if not dbook:
        raise HTTPException(status_code=404, detail='Book not found')

    
    dbook.name = book.name
    dbook.author = book.author
    dbook.year = book.year
    dbook.price = book.price
    dbook.availability = book.availability
    session.commit()

    return dbook


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id, session = Depends(get_db)):
    book = session.query(Book).get(id)
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
        
    session.delete(book)
    session.commit()

    return None
