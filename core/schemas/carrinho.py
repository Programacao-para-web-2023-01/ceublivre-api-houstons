from pydantic import BaseModel

class Carrinho(BaseModel):
    produto: int
    qtd: int
    usuario: int