from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import schemas, crud
from app.dependency import get_db
from typing import List


router = APIRouter()


@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    items = crud.get_items(db, skip=skip, limit=limit)
    return items
