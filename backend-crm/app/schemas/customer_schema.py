from pydantic import BaseModel
from datetime import datetime


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    city: str
    preferred_channel: str
    total_spend: float
    last_order_date: datetime

    class Config:
        from_attributes = True