from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    price: float
    quantity: int
    category: str


class ItemUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    quantity: int | None = None
    category: str | None = None


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    category: str