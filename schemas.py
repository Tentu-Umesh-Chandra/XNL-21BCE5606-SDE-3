from pydantic import BaseModel

class OrderSchema(BaseModel):
    order_id: int
    price: float
    quantity: int
    order_type: str
