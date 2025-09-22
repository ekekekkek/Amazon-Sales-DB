from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..db import get_db
from .. import models, schemas

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get("/", response_model=List[schemas.ReviewOut])
def get_reviews(
    db: Session = Depends(get_db),

    user_id: Optional[str] = Query(None, description="User ID"),
    product_id: Optional[str] = Query(None, description="Product ID")
):
    query = db.query(models.Review)

    if user_id:
        query = query.filter(models.Review.user_id == user_id)

    if product_id:
        query = query.filter(models.Review.product_id == product_id)

    if not user_id and not product_id:
        raise HTTPException(status_code=400, detail="Either user_id or product_id must be provided")

    reviews = query.all()
    return reviews[:100] # limit the number of reviews returned

@router.get("/{review_id}", response_model=schemas.ReviewOut)
def get_review(
    review_id: str,
    db: Session = Depends(get_db)
):
    review = db.get(models.Review, review_id)

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review