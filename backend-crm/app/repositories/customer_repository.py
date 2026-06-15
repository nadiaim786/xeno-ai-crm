from sqlalchemy.orm import Session
from app.models.customer import Customer


def get_customers(
    db: Session,
    skip: int = 0,
    limit: int = 20
):
    return (
        db.query(Customer)
        .offset(skip)
        .limit(limit)
        .all()
    )