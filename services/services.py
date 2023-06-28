from core.schemas.cart import *
from core.database.database import db
from core.database.dbprod import db as prod
from core.schemas.product import *
import json

def get_cart(key):
    cart = db.get(key)
    return cart


def get_user_cart(user):
    cart = db.fetch({"user": user}).items
    if cart:
        return cart[0]


def create_cart(cart):
    if get_user_cart(cart["user"]):
        return None
    
    new_cart = db.insert(cart)
    return new_cart


def add_product(key, product, quantity):
    cart = get_cart(key)
    if cart:
        item = Item(product=product, quantity=quantity)
        indice = exists_product(cart=cart, product=product)
        if indice == -1:
            cart["items"].append(item.dict())
            updated_cart = db.put(cart, key)
            if updated_cart:
                return updated_cart
        else:
            updated_cart = update_product_quantity(key, indice, item.dict())
            if updated_cart:
                return updated_cart

    return None


def update_product_quantity(key, indice, item):
    cart = get_cart(key)
    if cart:
        cart["items"][indice] = item
        updated_cart = db.put(cart, key)
        if updated_cart:
            return updated_cart

    return None


def update_cart(key, cart):
    try:
        db.update(cart, key)
        return cart
    except:
        return None
    

def exists_product(cart, product):
    items = cart["items"]
    indice = -1
    for i in range(len(items)):
        if items[i]["product"] == product:
            indice = i
            break

    return indice
    

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
        indice = exists_product(cart=cart, product=product)

        if indice >= 0:
            items.pop(indice)
            cart["items"] = items
            updated_cart = db.put(cart, key)
            if updated_cart:
                return updated_cart        
        
    return None


def get_product_id(id):
    return prod.get(id)


def create_product(produto):
    new_prod = prod.insert(produto)
    return new_prod


def get_product():
    return prod.fetch().items
