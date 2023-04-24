from pydantic import BaseModel

class Item(BaseModel):
    product: int
    quantity: int