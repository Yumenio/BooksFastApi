from cgi import test
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

database_url = 'sqlite:///booksdb.db'
engine = create_engine(database_url)
LocalSession = sessionmaker(bind=engine, expire_on_commit=False)

def get_db():
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()


# class Book(Base):
#     # name, year, author, price and availability(amount)
#     __tablename__ = 'Books'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     year = Column(Integer)
#     author = Column(String(20))
#     price = Column(Float)
#     availability = Column(Integer)