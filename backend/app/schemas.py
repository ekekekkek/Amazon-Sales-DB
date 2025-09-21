# backend/app/schemas.py -- defines how data moves in and out of API
# uses Pydantic models for validation, serialization, and documentation
# essentially, this cares about how FastAPI talks JSON to and from the database
from pydantic import BaseModel, Field
from typing import Optional, List

# ProductOut -- defines the output schema for the product
# ProductUpdate -- defines the input schema for the product
# ReviewCreate -- defines the input schema for the review
# UserCreate -- defines the input schema for the user
# UserOut -- defines the output schema for the user
# UserUpdate -- defines the input schema for the user

# from_attributes = True is only needed for schemas that read FROM the database
# Update and Create schemas don't need it because they 

class ProductOut(BaseModel):
    product_id: str = Field(..., description="The ID of the product")
    product_name: str = Field(None, description="The name of the product")
    category_path: str = Field(None, description="The path of the category")
    category_leaf: str = Field(None, description="The left of the category")
    discounted_price: float = Field(None, description="The discounted price of the product")
    actual_price: float = Field(None, description="The actual price of the product")
    discount_percentage: float = Field(None, description="The discount percentage of the product")
    rating: float = Field(None, description="The rating of the product")
    rating_count: int = Field(None, description="The number of ratings of the product")
    about_product: str = Field(None, description="The description of the product")
    img_link: str = Field(None, description="The link to the image of the product")
    product_link: str = Field(None, description="The link to the product")
    class Config: from_attributes = True

class ProductUpdate(BaseModel):
    product_name: str = Field(None, description="The name of the product")
    category_path: str = Field(None, description="The path of the category")
    category_leaf: str = Field(None, description="The left of the category")
    discounted_price: float = Field(None, description="The discounted price of the product")
    actual_price: float = Field(None, description="The actual price of the product")
    discount_percentage: float = Field(None, description="The discount percentage of the product")
    rating: float = Field(None, description="The rating of the product")
    rating_count: int = Field(None, description="The number of ratings of the product")
    about_product: str = Field(None, description="The description of the product")
    img_link: str = Field(None, description="The link to the image of the product")
    product_link: str = Field(None, description="The link to the product")

class ReviewCreate(BaseModel):
    review_id: str = Field(..., description="The ID of the review")
    product_id: str = Field(..., description="The ID of the product")
    user_id: str = Field(None, description="The ID of the user")
    user_name: str = Field(None, description="The name of the user")
    review_title: str = Field(None, description="The title of the review")
    review_content: str = Field(None, description="The content of the review")
    # doesn't need class Config: from_attributes = True because it's used to deserialize data INTO the database

class ReviewOut(BaseModel):
    review_id: str = Field(..., description="The ID of the review")
    product_id: str = Field(..., description="The ID of the product")
    user_id: str = Field(None, description="The ID of the user")
    user_name: str = Field(None, description="The name of the user")
    review_title: str = Field(None, description="The title of the review")
    review_content: str = Field(None, description="The content of the review")
    class Config: from_attributes = True # this is because ReviewOut is used to serialize dta FROM the database

class UserCreate(BaseModel):
    user_id: str = Field(..., description="The ID of the user")
    user_name: str = Field(None, description="The name of the user")

class UserOut(BaseModel):
    user_id: str = Field(..., description="The ID of the user")
    user_name: str = Field(None, description="The name of the user")
    class Config: from_attributes = True