from fastapi import APIRouter

from app.schemas.campaign_schema import (
    CampaignRequest
)

from app.services.campaign_service import (
    generate_campaign,
    send_campaign_to_channel_service
)

router = APIRouter(
    prefix="/campaign",
    tags=["Campaign"]
)


@router.post("/generate")
def create_campaign(
    request: CampaignRequest
):

    campaign = generate_campaign(
        request.goal
    )

    send_result = (
        send_campaign_to_channel_service(
            recipient=
            "customer@gmail.com",

            message=
            campaign[
                "campaign_message"
            ],

            channel=
            campaign[
                "recommended_channel"
            ]
        )
    )

    return {
        "campaign_goal":
        request.goal,

        **campaign,

        "delivery_status":
        send_result
    }