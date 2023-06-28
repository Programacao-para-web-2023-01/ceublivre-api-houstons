from fastapi import FastAPI, HTTPException
import services.services as services


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "api em construção"}

@app.get("/cart/{key}")
async def root(key: str):
    cart = services.get_cart(key)
    if cart:
        return cart
    
    raise HTTPException(status_code=404, detail="Cart not found")


@app.get("/cart/user/{user}")
async def get_cart(user: int):
    item = services.get_user_cart(user)
    if item:
        return item
    
    raise HTTPException(status_code=404, detail="User does not have an active cart")


@app.post("/cart")
async def create_cart(cart: services.Cart):
    exists_cart = services.get_user_cart(cart.user)
    if exists_cart:
        cart = services.update_cart(exists_cart["key"], cart.dict())
        return cart

    new_cart = services.create_cart(cart.dict())
    if new_cart:
        return new_cart
    
    raise HTTPException(status_code=404, detail="User has active cart")


@app.put("/cart/{key}")
async def put_cart(key: str, cart: services.Cart):
    cart = services.update_cart(key, cart.dict())
    if cart:
        return cart
    
    raise HTTPException(status_code=404, detail="Product not found in the cart")

@app.put("/cart/{key}/items/product/{product}/quantity/{quantity}")
async def add_product(key: str, product: str, quantity: int):
    cart = services.add_product(key, product, quantity)
    if cart:
        return cart

    raise HTTPException(status_code=404, detail="Product does not exist")


@app.delete("/cart/{key}")
async def delete_cart(key: str):
    delete = services.delete_cart(key)
    if delete:
        return {"detail": "deleted with success"}
    
    raise HTTPException(status_code=404, detail="Cart not found")


@app.delete("/cart/{key}/item/product/{product}")
async def delete_cart_product(key: str, product: str):
    cart = services.delete_cart_product(key, product)
    if cart: 
        return cart
    
    raise HTTPException(status_code=404, detail="Item not found in the Cart")


@app.get('/product')
async def get_product():
    prod = services.get_product()
    if prod:
        return prod
    
    raise HTTPException(status_code=404, detail="Products not found")


@app.get('/product/{id}')
async def get_product_id(id:str):
    prod = services.get_product_id(id)
    if prod:
        return prod
    
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/product")
async def create_product(product: services.Product):

    new_product = services.create_product(product.dict())
    if new_product:
        return new_product
    
    raise HTTPException(status_code=404, detail="Product has active cart")
