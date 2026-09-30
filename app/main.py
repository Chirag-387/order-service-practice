from fastapi import FastAPI
import httpx
from httpx import HTTPStatusError, RequestError

app = FastAPI()

@app.get("/")
def check():
    return {
        "message": "Main backend is running"
    }

@app.post("/test-order")
def test_order():
    try:
        response = httpx.post("http://127.0.0.1:8001/orders")
        response.raise_for_status()
        return response.json()
    except HTTPStatusError:
        return {
            "message": "The Order Service responded, but with an error status like 404"
        }
    except RequestError:
        return {
            "message": "The Main Backend couldn't successfully communicate with the Order Service"
        }