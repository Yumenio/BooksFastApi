# import ..db

# from sqlalchemy import Column, Integer, String, Float, Date

# class Book(db.Base):
#     # name, year, author, price and availability(amount)
#     __tablename__ = 'Books'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     year_published = Column(Date)
#     author = Column(String(20), nullable=False)
#     price = Column(Float, nullable=False)
#     availability = Column(Integer, nullable=False)