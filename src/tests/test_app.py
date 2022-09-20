# from fastapi.testclient import TestClient
# from ..db import Base, test_engine, TestSession
# from ..main import app

# Base.metadata.create_all(test_engine)

def test_root(client):
    ans = client.get("/")
    # assert ans.status_code==200
    assert ans.json() == {'msg': 'Hello World'}

# def test_create(client):
#     ans = client.post(
#         "/books",
#         json={
#             "id": 1,
#             "name": "string",
#             "author": "string",
#             "year": 0,
#             "price": 0,
#             "availability": 0
#         }
#         )
    
#     assert ans.status_code == 201
#     assert ans.json() == {
#         "id": 1,
#         "name": "string",
#         "author": "string",
#         "year": 0,
#         "price": 0,
#         "availability": 0
#     }


# def test_read(client):
#     ans = client.get("/books/1")
#     assert ans.status_code == 200
#     assert ans.json() == {"id":1,"name":"string","author":"string","year":0,"price":0.0,"availability":0}
