from fastapi import FastAPI
from fastapi import status


app = FastAPI()

@app.get("/")
def root():
    return {"msg" : "Hello World"}

@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book():
    return "create"

@app.get("/books/{id}")
def read_book(id):
    return "read"

@app.put("/books/{id}")
def update_book(id):
    return "update"

@app.delete("/books/{id}")
def delete_book(id):
    return "delete"

@app.get("/books")
def read_books_list():
    return "read list"