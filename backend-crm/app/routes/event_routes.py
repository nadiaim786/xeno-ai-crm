from fastapi import APIRouter

from app.schemas.event_schema import (
    CampaignEvent
)

router = APIRouter(
    prefix="/campaign",
    tags=["Campaign Events"]
)

# temporary in-memory analytics
campaign_metrics = {
    "sent": 0,
    "delivered": 0,
    "opened": 0,
    "clicked": 0,
    "converted": 0,
    "failed": 0
}


@router.post("/event")
def receive_event(
    event: CampaignEvent
):

    status = event.status

    if status in campaign_metrics:
        campaign_metrics[
            status
        ] += 1

    print(
        "Campaign Event Received:",
        event.dict()
    )

    return {
        "message":
        "Event received"
    }


@router.get("/analytics")
def get_analytics():

    total_sent = (
        campaign_metrics["sent"]
    )

    ctr = 0
    conversion_rate = 0

    if total_sent > 0:

        ctr = round(
            (
                campaign_metrics[
                    "clicked"
                ]
                / total_sent
            ) * 100,
            2
        )

        conversion_rate = round(
            (
                campaign_metrics[
                    "converted"
                ]
                / total_sent
            ) * 100,
            2
        )

    return {
        **campaign_metrics,

        "ctr":
        f"{ctr}%",

        "conversion_rate":
        f"{conversion_rate}%"
    }