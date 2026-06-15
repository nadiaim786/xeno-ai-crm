from fastapi import FastAPI

from app.routes.channel_routes import (
    router as channel_router
)

app = FastAPI(
    title="XenoReach Channel Service"
)

app.include_router(
    channel_router
)


@app.get("/")
def home():

    return {
        "message":
        "Channel Service Running"
    }