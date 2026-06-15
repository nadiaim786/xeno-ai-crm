from pydantic import BaseModel


class MessageRequest(
    BaseModel
):
    recipient: str
    message: str
    channel: str
    campaign_id: int = 1