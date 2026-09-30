from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def order():
    return {
        "message": "Order service is running"
    }

@app.post("/orders")
def create_order():
    return {
        "order_id": 101,
        "status": "created"
    }