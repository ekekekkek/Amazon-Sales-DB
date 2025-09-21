from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..db import get_db
from .. import models, schemas

# Groups all endpoints under /products
router = APIRouter(prefix="/products", tags=["products"])

# Retrieves multiple products based on optional filters
@router.get("/", response_model=List[schemas.ProductOut]) # returns a list of ProductOut objects
def get_products(
    db: Session = Depends(get_db), # Dependencies: each request gets a database session from db.py
    
    # Query paramters -- optional filters -- always match to model fields
    category_leaf: Optional[str] = Query(None, description="The leaf of the category"),
    category_path: Optional[str] = Query(None, description="The path of the category"),
):
    # Query the database
    query = db.query(models.Product)

    # Apply filters
    if category_leaf:
        query = query.filter(models.Product.category_leaf == category_leaf)
    if category_path:
        query = query.filter(models.Product.category_path == category_path)

    # Execute the query
    products = query.all()
    return products[:100] # limit the number of products returned

# Retrieves a single product by ID
@router.get("/{product_id}", response_model=schemas.ProductOut)
def get_product(
    product_id: str, # Path parameter from URL
    db: Session = Depends(get_db) # Dependencies
):
    prod = db.get(models.Product, product_id) 

    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod

# Other endpoints to be added