from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Demo API")

class Item(BaseModel):
    name: str
    price: float

items_db = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[item_id] = item.model_dump()
    return {"id": item_id, **items_db[item_id]}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items_db[item_id]}
