from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///booksdb.db')
Base = declarative_base()
LocalSession = sessionmaker(bind=engine, expire_on_commit=False)



class Book(Base):
    # name, year, author, price and availability(amount)
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # year_published = Column(DateTime)
    author = Column(String(20))
    price = Column(Float)
    availability = Column(Integer)