from fastapi import FastAPI
from app.database.db import engine, Base
from app.routers import item_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(item_router.router)


@app.get("/")
def home():
    return {"message": "Inventory API running"}



