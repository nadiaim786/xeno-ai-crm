from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from datetime import datetime

from app.core.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True
    )

    phone = Column(
        String(20)
    )

    city = Column(
        String(100)
    )

    preferred_channel = Column(
        String(50)
    )

    total_spend = Column(
        Float,
        default=0
    )

    last_order_date = Column(
        DateTime
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )