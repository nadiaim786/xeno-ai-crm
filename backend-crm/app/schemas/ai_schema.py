from pydantic import BaseModel


class SegmentRequest(BaseModel):
    prompt: str