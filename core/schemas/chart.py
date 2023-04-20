from pydantic import BaseModel
from core.schemas.products import Products
from typing import List

class Chart(BaseModel):
    user: int
    items: List[Products]