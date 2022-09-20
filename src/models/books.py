from ..db import Base
from sqlalchemy import Column, Integer, String, Float

class Book(Base):
    # name, year, author, price and availability(amount)
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    year = Column(Integer)
    author = Column(String(20))
    price = Column(Float)
    availability = Column(Integer)