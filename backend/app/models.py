# backend/app/models.py -- defines the tables as Python classes, 
# so they can be used to interact with the database using SQLAlchemy ORM
# think of this as a boilerplate for the database tables
# this defines how data is stored in the database(tables, columns, relationships)
from sqlalchemy import Column, Text, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Text, primary_key = True)
    product_name = Column(Text, nullable=True)
    category_path = Column(Text)
    category_leaf = Column(Text)
    discounted_price = Column(Numeric(12,2))
    actual_price = Column(Numeric(12,2))
    discount_percentage = Column(Numeric(5,2))
    rating = Column(Numeric(3,2))
    rating_count = Column(Integer)
    about_product = Column(Text)
    img_link = Column(Text)
    product_link = Column(Text)

class Review(Base):
    __tablename__ = "reviews"
    review_id = Column(Text, primary_key = True)
    product_id = Column(Text, ForeignKey("products.product_id"), nullable=False)
    user_id = Column(Text, ForeignKey("users.user_id"), nullable=True)
    user_name = Column(Text, nullable=True)
    review_title = Column(Text, nullable=True)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Text, primary_key = True)
    user_name = Column(Text, nullable=True)