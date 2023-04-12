from core.schemas.carrinho import *
from core.database.database import db

def get_carrinho_usuario(user):
    items = db.fetch({"usuario": user}).items
    return items


def update_qtd_carrinho(user, prod, carrinho):
    item = db.fetch({"usuario": user, "produto": prod}).items
    if item:
        key = item[0]["key"]
        db.update(carrinho, key)
        return carrinho