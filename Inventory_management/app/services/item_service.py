from sqlalchemy.orm import Session
from app.models.item_model import Item
from app.schemas.item_schema import ItemCreate


def create_item(db: Session, item: ItemCreate):
    new_item = Item(
        name=item.name,
        price=item.price,
        quantity=item.quantity,
        category=item.category
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


def get_items(db: Session):
    return db.query(Item).all()


def delete_item(db: Session, item_id: int):

    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise ValueError("Item not found")

    db.delete(item)
    db.commit()


def update_item(db: Session, item_id: int, data):

    item = db.query(Item).filter(Item.id == item_id).first()

    if not item:
        raise ValueError("Item not found")

    if data.name:
        item.name = data.name

    if data.category:
        item.category = data.category

    db.commit()
    db.refresh(item)

    return item