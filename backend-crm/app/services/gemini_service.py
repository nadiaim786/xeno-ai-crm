import json
import google.generativeai as genai

from app.core.config import (
    GEMINI_API_KEY
)

# Configure Gemini
genai.configure(
    api_key=GEMINI_API_KEY
)

# Debug check
print("Gemini Key:", GEMINI_API_KEY)

# Model
model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


def parse_customer_intent(
    prompt: str
):
    """
    Convert marketer natural language
    into structured CRM filters.
    """

    system_prompt = f"""
You are an AI CRM segmentation assistant.

Convert marketer intent into JSON filters.

Allowed keys:
city
min_spend
inactive_days
category

Return ONLY valid JSON.

User prompt:
{prompt}

Example:

{{
    "city": "Chennai",
    "min_spend": 5000,
    "inactive_days": 45
}}
"""

    try:

        response = model.generate_content(
            system_prompt
        )

        text = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        print("Gemini Segmentation Response:", text)

        return json.loads(text)

    except Exception as e:

        print(
            "Gemini Segmentation Error:",
            e
        )

        return None