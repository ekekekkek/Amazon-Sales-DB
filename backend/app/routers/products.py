from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..db import get_db
from .. import models, schemas
import uuid

# Groups all endpoints under /products
router = APIRouter(prefix="/products", tags=["products"])

# Retrieves multiple products based on optional filters
@router.get("/", response_model=List[schemas.ProductOut]) # returns a list of ProductOut objects
def get_products(
    db: Session = Depends(get_db), # Dependencies: each request gets a database session from db.py
    
    # Query paramters -- optional filters -- always match to model fields
    category: Optional[str] = Query(None, description="Category")
):
    # Query the database
    query = db.query(models.Product)

    # Apply filters
    if category:
        query = query.filter(models.Product.category == category)

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

# Creates a product
@router.post("/", response_model=schemas.ProductOut)
def create_product(
    payload: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    product_data = payload.model_dump()
    product_data["product_id"] = str(uuid.uuid4())
    prod = models.Product(**product_data)
    
    db.add(prod)
    db.commit()
    db.refresh(prod)
    return prod

# Updates a product -- since we're updating an existing product, we use PUT instead of POST
# returns a ProductOut object because we're returning the updated product
# not schemas.ProductUpdate because ProductUpdate is the request body, not response body
@router.put("/{product_id}", response_model=schemas.ProductOut) 
def update_product(
    product_id: str,
    payload: schemas.ProductUpdate, # request body -- contains the field to update
    db: Session = Depends(get_db)
):
    prod = db.get(models.Product, product_id)

    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for field, value in payload.model_dump().items():
        # prod = product object from DB
        # field = name of attribute to update e.g., product_name, category
        # value = new value for the attribute
        setattr(prod, field, value)

    db.commit()
    db.refresh(prod)
    return prod

# Delete a product
@router.delete("/{product_id}", response_model=schemas.ProductOut)
def delete_product(
    product_id: str,
    db: Session = Depends(get_db)
):
    prod = db.get(models.Product, product_id)

    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(prod)
    db.commit()
    return prod