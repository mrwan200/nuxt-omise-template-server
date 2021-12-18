from pydantic import BaseModel

class PaymentRequest(BaseModel):
    name: str
    email: str
    phone: str
    amount: int
    token: str
