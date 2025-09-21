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
    category = Column(Text)
    discounted_price = Column(Text)
    actual_price = Column(Text)
    discount_percentage = Column(Text)
    rating = Column(Text)
    rating_count = Column(Text)
    about_product = Column(Text)
    img_link = Column(Text)
    product_link = Column(Text)

class Review(Base):
    __tablename__ = "reviews"
    review_id = Column(Text, primary_key = True)
    product_id = Column(Text, ForeignKey("products.product_id"), nullable=False)
    user_id = Column(Text, ForeignKey("users.user_id"), nullable=False)
    user_name = Column(Text)
    review_title = Column(Text)
    review_content = Column(Text)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Text, primary_key = True)
    user_name = Column(Text)