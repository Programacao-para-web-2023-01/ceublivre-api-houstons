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


@app.delete("/cart/{key}")
async def delete_cart(key: str):
    delete = services.delete_cart(key)
    if delete:
        return {"detail": "deleted with success"}
    
    raise HTTPException(status_code=404, detail="Cart not found")


@app.delete("/cart/{key}/item/product/{product}")
async def delete_cart_product(key: str, product: int):
    cart = services.delete_cart_product(key, product)
    if cart: 
        return cart
    
    raise HTTPException(status_code=404, detail="Item not found in the Cart")