from pydantic import BaseModel


class CampaignEvent(
    BaseModel
):
    campaign_id: int
    recipient: str
    channel: str
    status: str