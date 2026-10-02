from fastapi import FastAPI
from pydantic import BaseModel

class Order(BaseModel):
    product: str
    quantity: int

app = FastAPI()

@app.get("/")
def order():
    return {
        "message": "Order service is running"
    }

@app.post("/orders")
def create_order(order: Order):
    return {
        "product": order.product,
        "quantity": order.quantity,
    }