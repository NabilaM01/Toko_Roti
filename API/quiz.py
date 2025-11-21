from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Model data
class Item(BaseModel):
    nama: Optional[str] = None
    nim: Optional[int] = None
    jurusan: Optional[str] = None
    semester: Optional[int] = None
    ipk: Optional[int] = None
    alamat: Optional[str] = None
    

# Simulasi database (bungkusan model data)
items_db = {}

# ROOT
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# CREATE (POST) -> membuat data
@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id in items_db:
        return {"error": "Item already exists"}
    items_db[item_id] = item.dict()
    return {"message": "Item created successfully", "item": items_db[item_id]}

# READ (GET) -> melihat data yang sudah dibuat
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items_db:
        return {"error": "Item not found"}
    return {"item_id": item_id, "item": items_db[item_id]}

# UPDATE (PUT) -> memperbaikin / update data yang sudah dibuat
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        return {"error": "Item not found"}
    items_db[item_id] = item.dict()
    return {"message": "Item updated successfully", "item": items_db[item_id]}

# DELETE (DELETE)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        return {"error": "Item not found"}
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted successfully", "deleted_item": deleted_item}