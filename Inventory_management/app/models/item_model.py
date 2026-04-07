from app.database.db import Base
from sqlalchemy import Column, Integer, String, Float

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    price = Column(Float)        # ✅ ADD THIS
    quantity = Column(Integer)   # ✅ ADD THIS
    category = Column(String)