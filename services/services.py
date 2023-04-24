from core.schemas.cart import *
from core.database.database import db

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


# def delete_cart_product(key, product):
#     cart = get_cart(key)
#     cart_dict = dict(cart)
#     if cart_dict:
#         for i in range(len(cart_dict["items"]["product"])):
#             if cart_dict["items"]["product"][i] == product:
#                 del cart_dict["items"]["product"][i]
#                 return cart_dict
        
#     return None