from pydantic import BaseModel
from core.schemas.item import Item
from typing import List

class Cart(BaseModel):
    user: int
    items: List[Item]