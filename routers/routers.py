from fastapi import FastAPI, HTTPException
import services.services as services

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "api em construção"}


@app.get("/carrinho/{user}")
async def get_carrinho(user: int):
    item = services.get_carrinho_usuario(user)
    if item:
        return item
    
    raise HTTPException(status_code=404, detail="Usuário não tem carrinho ativo")