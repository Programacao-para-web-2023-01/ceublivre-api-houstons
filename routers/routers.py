from fastapi import FastAPI, HTTPException
import services.services as services


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "api em construção"}


@app.get("/carrinho/user/{user}")
async def get_carrinho(user: int):
    item = services.get_carrinho_usuario(user)
    if item:
        return item
    
    raise HTTPException(status_code=404, detail="User does not have an active cart")


@app.put("/carrinho/user/{user}/product/{prod}")
async def put_qtd_carrinho(user: int, prod: int, carrinho: services.Carrinho):
    if user != carrinho.usuario:
        raise HTTPException(status_code=404, detail="User from path is not equals to body User")
    
    if prod != carrinho.produto:
        raise HTTPException(status_code=404, detail="Product from path is not equals to body Product")
    
    item = services.update_qtd_carrinho(user, prod, carrinho.dict())
    if item:
        return item
    
    raise HTTPException(status_code=404, detail="Product not found in the chart")