# from fastapi.testclient import TestClient
# from ..db import Base, test_engine, TestSession
# from ..main import app

# Base.metadata.create_all(test_engine)

def test_create(client):
    ans = client.post(
        "/books/books",
        json={
            "name": "string",
            "author": "string",
            "year": 0,
            "price": 0,
            "availability": 0
        }
        )
    
    assert ans.status_code == 201
    assert ans.json() == {
        "id": 1,
        "name": "string",
        "author": "string",
        "year": 0,
        "price": 0,
        "availability": 0
    }


def test_read(client):
    ans = client.post(
        "/books/books",
        json={
            "name": "string",
            "author": "string",
            "year": 0,
            "price": 0,
            "availability": 0
        }
        )
    ans = client.get("/books/1")
    assert ans.status_code == 200
    assert ans.json() == {"id":1,"name":"string","author":"string","year":0,"price":0.0,"availability":0}

def test_read_all(client):
    ans = client.get("/books/")
    
# def test_update(client):
#     data = {
#         "name": "string",
#         "author": "string",
#         "year": 0,
#         "price": 0,
#         "availability": 0
#     }
#     ans = client.post(
#         "/books/books",
#         json=data
#         )
#     assert ans.status_code == 201

#     data["name"] = "brandon"

#     ans = client.put(
#         "/books/1",
#         json=data
#     )
#     assert ans.status_code == 200
#     assert ans.json() == { "id": 1, "name": "twok", "author": "brandon sanderson", "year": 2011, "price": 13.55, "availability": 6 }

def test_delete(client):
    data = {
        "name": "string",
        "author": "string",
        "year": 0,
        "price": 0,
        "availability": 0
    }
    ans = client.post("/books/books", json=data)
    assert ans.status_code == 201

    ans = client.delete("/books/1")
    assert ans.status_code == 204