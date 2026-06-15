from fastapi import APIRouter
from threading import Thread

from app.schemas.message_schema import (
    MessageRequest
)

from app.services.simulator_service import (
    simulate_message_flow
)

router = APIRouter(
    prefix="/channel",
    tags=["Channel Service"]
)


@router.post("/send")
def send_message(
    request: MessageRequest
):

    Thread(
        target=simulate_message_flow,
        args=(request.dict(),)
    ).start()

    return {
        "message":
        "Campaign queued",

        "recipient":
        request.recipient,

        "channel":
        request.channel
    }