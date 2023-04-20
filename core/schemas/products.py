from pydantic import BaseModel

class Products(BaseModel):
    product: int
    quantity: int