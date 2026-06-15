from datetime import datetime
from datetime import timedelta

from sqlalchemy.orm import Session
from app.models.customer import Customer


def interpret_prompt(prompt: str):

    prompt = prompt.lower()

    filters = {}

    if "chennai" in prompt:
        filters["city"] = "Chennai"

    if "bangalore" in prompt:
        filters["city"] = "Bangalore"

    if "premium" in prompt:
        filters["min_spend"] = 5000

    if "inactive" in prompt:
        filters["inactive_days"] = 45

    return filters


def segment_customers(
    db: Session,
    filters: dict
):

    query = db.query(Customer)

    if "city" in filters:
        query = query.filter(
            Customer.city ==
            filters["city"]
        )

    if "min_spend" in filters:
        query = query.filter(
            Customer.total_spend >=
            filters["min_spend"]
        )

    if "inactive_days" in filters:

        cutoff_date = (
            datetime.now()
            - timedelta(
                days=filters["inactive_days"]
            )
        )

        query = query.filter(
            Customer.last_order_date
            <= cutoff_date
        )

    customers = query.all()

    avg_spend = 0

    if customers:
        avg_spend = round(
            sum(
                c.total_spend
                for c in customers
            ) / len(customers),
            2
        )

    return {
        "interpreted_filters": filters,
        "audience_size": len(customers),
        "avg_spend": avg_spend,
        "sample_customers": [
            {
                "name": c.name,
                "city": c.city,
                "total_spend": c.total_spend
            }
            for c in customers[:5]
        ]
    }