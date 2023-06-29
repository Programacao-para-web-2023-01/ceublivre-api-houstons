from pydantic import BaseModel

class Item(BaseModel):
    product: str
    quantity: int