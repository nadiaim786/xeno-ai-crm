from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.ai_schema import SegmentRequest

from app.services.segmentation_service import (
    interpret_prompt,
    segment_customers
)

from app.services.gemini_service import (
    parse_customer_intent
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post("/segment")
def ai_segment(
    request: SegmentRequest,
    db: Session = Depends(get_db)
):

    filters = parse_customer_intent(
        request.prompt
    )

    if not filters:
        filters = interpret_prompt(
            request.prompt
        )

    result = segment_customers(
        db,
        filters
    )

    return {
        "input": request.prompt,
        **result
    }