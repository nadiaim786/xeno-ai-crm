from faker import Faker
from random import choice
from random import randint
from random import uniform
from datetime import datetime
from datetime import timedelta

from app.core.database import SessionLocal
from app.models.customer import Customer
from app.models.order import Order

fake = Faker("en_IN")

db = SessionLocal()

cities = [
    "Chennai",
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Pune",
    "Kolkata",
    "Ahmedabad"
]

channels = [
    "WhatsApp",
    "SMS",
    "Email",
    "RCS"
]

categories = [
    "Fashion",
    "Beauty",
    "Coffee",
    "Skincare",
    "Electronics"
]


def seed_customers():

    customers = []

    for _ in range(300):

        customer = Customer(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            city=choice(cities),
            preferred_channel=choice(channels),
            total_spend=round(
                uniform(500, 25000),
                2
            ),
            last_order_date=datetime.now()
            - timedelta(days=randint(1, 180))
        )

        customers.append(customer)

    db.add_all(customers)
    db.commit()

    print("300 customers inserted")


def seed_orders():

    customers = db.query(Customer).all()

    orders = []

    for customer in customers:

        total_orders = randint(1, 7)

        for _ in range(total_orders):

            order = Order(
                customer_id=customer.id,
                amount=round(
                    uniform(200, 8000),
                    2
                ),
                category=choice(categories),
                order_date=datetime.now()
                - timedelta(days=randint(1, 180))
            )

            orders.append(order)

    db.add_all(orders)
    db.commit()

    print(f"{len(orders)} orders inserted")


if __name__ == "__main__":

    seed_customers()
    seed_orders()