from core.schemas.cart import *
from core.database.database import db
import json

def get_cart(key):
    cart = db.get(key)
    return cart


def get_user_cart(user):
    items = db.fetch({"user": user}).items
    return items


def create_cart(cart):
    if get_user_cart(cart["user"]):
        return None
    
    new_cart = db.insert(cart)
    return new_cart


def update_cart(key, cart):
    try:
        db.update(cart, key)
        return cart
    except:
        return None
    

def delete_cart(key):
    cart = get_cart(key)
    if cart:
        db.delete(key)
        return True
    
    return False


def delete_cart_product(key, product):
    cart = get_cart(key)
    if cart:
        items = cart["items"]
        indice = -1
        for i in range(len(items)):
            if items[i]["product"] == product:
                indice = i
                break

        if indice >= 0:
            items.pop(indice)
            cart["items"] = items
            updated_cart = db.put(cart, key)
            if updated_cart:
                return updated_cart        
        
    return None