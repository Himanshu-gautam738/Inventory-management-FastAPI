from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.item_schema import ItemCreate, ItemUpdate
from app.services import item_service

router = APIRouter()


@router.post("/items")
def add_item(item: ItemCreate, db: Session = Depends(get_db)):

    try:
        return item_service.create_item(db, item)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/items")
def display_items(db: Session = Depends(get_db)):
    return item_service.get_items(db)


@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):

    try:
        item_service.delete_item(db, item_id)
        return {"message": "Item deleted"}

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/items/{item_id}")
def update_item(item_id: int, data: ItemUpdate, db: Session = Depends(get_db)):

    try:
        return item_service.update_item(db, item_id, data)

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))