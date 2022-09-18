from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date

engine = create_engine('sqlite:///booksdb.db')
Base = declarative_base()



class Book(Base):
    # name, year, author, price and availability(amount)
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # year_published = Column(Date)
    # author = Column(String(20), nullable=False)
    # price = Column(Float, nullable=False)
    # availability = Column(Integer, nullable=False)