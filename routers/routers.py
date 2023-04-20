from fastapi import FastAPI, HTTPException
import services.services as services


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "api em construção"}

@app.get("/chart/{key}")
async def root(key: str):
    chart = services.get_chart(key)
    if chart:
        return chart
    
    raise HTTPException(status_code=404, detail="Chart not found")


@app.get("/chart/user/{user}")
async def get_chart(user: int):
    item = services.get_user_chart(user)
    if item:
        return item
    
    raise HTTPException(status_code=404, detail="User does not have an active cart")


@app.put("/chart/{key}")
async def put_qtd_chart(key: str, chart: services.Chart):
    chart = services.update_chart_quantity(key, chart.dict())
    if chart:
        return chart
    
    raise HTTPException(status_code=404, detail="Product not found in the chart")


@app.delete("/chart/{key}")
async def delete_product(key: str):
    delete = services.delete_chart(key)
    if delete:
        return {"detail": "deleted with success"}
    
    raise HTTPException(status_code=404, detail="Chart not found")