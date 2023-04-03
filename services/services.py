from core.schemas.carrinho import *
import core.database.database as db

def get_carrinho_usuario(user):
    items = db.db.fetch({"usuario": user}).items
    return items