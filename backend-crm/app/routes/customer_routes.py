from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.customer_schema import CustomerResponse
from app.repositories.customer_repository import get_customers

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.get(
    "/",
    response_model=List[CustomerResponse]
)
def fetch_customers(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    return get_customers(
        db,
        skip,
        limit
    )