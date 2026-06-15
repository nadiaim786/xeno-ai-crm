from pydantic import BaseModel


class CampaignRequest(BaseModel):
    goal: str