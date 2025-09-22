from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..db import get_db
from .. import models, schemas

# Groups all endpoints under /users
router = APIRouter(prefix="/users", tags=["users"])

# Retrieves list of users based on optional filters
# Query parameters: we want to filter/search multiple at once
@router.get("/", response_model=List[schemas.UserOut])
def get_users(
    db: Session = Depends(get_db),

    user_id: Optional[str] = Query(None, description="User ID")
):
    # Query the database
    query = db.query(models.User)

    # Apply filters
    if user_id:
        query = query.filter(models.User.user_id == user_id)

    # Execute the query
    users = query.all()
    return users[:100] # limit the number of users returned

# Retrieves a single user by ID, ID required
# Path parameter: we want to filter/search one at a time, so we need "/{user_id}" instead of just "/"
@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(
    user_id: str,
    db: Session = Depends(get_db)
):
    user = db.get(models.User, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Updates a user -- since we're updating an existing user, we use PUT instead of POST
# returns a UserOut object because we're returning the updated user
# not schemas.UserUpdate because UserUpdate is the request body, not response body
@router.put("/{user_id}", response_model=schemas.UserOut)
def update_user(
    user_id: str, # since this is a path parameter, we need "/{user_id}" instead of just "/"
    payload: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    user = db.get(models.User, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for field, value in payload.model_dump().items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user