import omise
import random
import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from model.paymentRequest import PaymentRequest

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Omise setup
with open("./config.json", "r") as f:
    config = json.load(f)
    omise.api_secret = config["omise"]["secret"]

# Fake Item
items = [{
    "id": 1,
    "name": "Item 1",
    "price": 150000
},
{
    "id": 2,
    "name": "Item 2",
    "price": 250000
},
{
    "id": 3,
    "name": "Item 3",
    "price": 500000
}]

@app.get("/items/list")
async def item():
    """
        Get Item List
    """
    return items
    
@app.post("/payment")
async def payment(pay: PaymentRequest):
    """
        Check Payment (Omise create charge)
    """
    token = omise.Charge.create(
        amount=pay.amount,
        currency='THB',
        card=pay.token
    )
    
    if token.status == "successful":
        return JSONResponse(
            status_code=200,
            content={
                "id": str(random.randint(10000000, 99999999)),
            }
        )
    
    return JSONResponse(
        status_code=402
    )
        
