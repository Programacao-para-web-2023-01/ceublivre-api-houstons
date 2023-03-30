from fastapi import FastAPI
import uvicorn
from core.database import database as db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "api em construção"}

@app.get("/carrinho")
async def carrinho():
    item = db.db.fetch().items
    return item

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)