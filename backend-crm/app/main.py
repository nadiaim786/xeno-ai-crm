from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.ai_routes import (
    router as ai_router
)

from app.routes.campaign_routes import (
    router as campaign_router
)

from app.routes.customer_routes import (
    router as customer_router
)

from app.routes.event_routes import (
    router as event_router
)

from app.core.database import (
    engine,
    Base
)

from app.models.customer import (
    Customer
)

from app.models.order import (
    Order
)

app = FastAPI(
    title="XenoReach AI CRM"
)

# CORS FIX
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message":
        "XenoReach AI Backend Running"
    }


app.include_router(
    campaign_router
)

app.include_router(
    customer_router
)

app.include_router(
    ai_router
)

app.include_router(
    event_router
)

Base.metadata.create_all(
    bind=engine
)