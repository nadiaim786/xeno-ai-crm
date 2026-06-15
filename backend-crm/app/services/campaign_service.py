import json
import requests
import google.generativeai as genai

from app.core.config import (
    GEMINI_API_KEY
)

# Configure Gemini
genai.configure(
    api_key=GEMINI_API_KEY
)

# Gemini model
model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


def smart_campaign_fallback(
    goal: str
):
    """
    Rule-based fallback campaign generation
    when Gemini fails/rate limits.
    """

    goal_lower = goal.lower()

    channel = "WhatsApp"

    reason = (
        "High engagement channel"
    )

    discount = "10%"

    # Premium shoppers
    if "premium" in goal_lower:
        discount = "15%"

    # Win-back / dormant campaigns
    if (
        "inactive" in goal_lower
        or "dormant" in goal_lower
        or "win back" in goal_lower
    ):

        message = (
            f"Hi {{{{name}}}}, "
            f"we miss you! "
            f"Enjoy {discount} OFF "
            f"on your next purchase ❤️"
        )

        reason = (
            "WhatsApp performs best "
            "for dormant shopper "
            "re-engagement"
        )

    # Sale campaigns
    elif "sale" in goal_lower:

        channel = "SMS"

        message = (
            "Hi {{{{name}}}}, "
            "exclusive offers are live! "
            "Shop now before stock runs out."
        )

        reason = (
            "SMS works well for "
            "urgent promotional campaigns"
        )

    # Generic engagement
    else:

        channel = "Email"

        message = (
            "Hi {{{{name}}}}, "
            "we have something special "
            "for you. Check out "
            "our latest collection!"
        )

        reason = (
            "Email supports richer "
            "customer engagement"
        )

    return {
        "recommended_channel":
        channel,

        "reason":
        reason,

        "campaign_message":
        message,

        "generation_mode":
        "smart_fallback"
    }


def generate_campaign(
    goal: str
):
    """
    Try Gemini campaign generation.
    Fall back to smart rules
    if Gemini fails.
    """

    prompt = f"""
You are an expert CRM marketing assistant.

Generate a shopper engagement campaign.

Return ONLY valid JSON.

Fields:
recommended_channel
reason
campaign_message

Campaign Goal:
{goal}
"""

    try:

        response = model.generate_content(
            prompt
        )

        text = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        print(
            "Gemini Campaign Response:",
            text
        )

        result = json.loads(
            text
        )

        result[
            "generation_mode"
        ] = "gemini"

        return result

    except Exception as e:

        print(
            "Campaign Gemini Error:",
            e
        )

        return smart_campaign_fallback(
            goal
        )


def send_campaign_to_channel_service(
    recipient: str,
    message: str,
    channel: str
):
    """
    Send campaign message
    to channel simulator service.
    """

    payload = {
        "recipient":
        recipient,

        "message":
        message,

        "channel":
        channel,

        "campaign_id":
        1
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8001/channel/send",
            json=payload
        )

        return response.json()

    except Exception as e:

        print(
            "Channel Service Error:",
            e
        )

        return {
            "error":
            "Channel service unavailable"
        }