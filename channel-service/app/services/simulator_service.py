import random
import time
import requests


CRM_CALLBACK_URL = (
    "http://127.0.0.1:8000/"
    "campaign/event"
)


def simulate_message_flow(
    payload: dict
):

    lifecycle = [
        "sent",
        "delivered"
    ]

    if random.random() > 0.2:
        lifecycle.extend([
            "opened",
            "clicked"
        ])

    if random.random() > 0.5:
        lifecycle.append(
            "converted"
        )

    if random.random() < 0.1:
        lifecycle = ["failed"]

    for status in lifecycle:

        time.sleep(2)

        callback_payload = {
            "campaign_id":
            payload["campaign_id"],

            "recipient":
            payload["recipient"],

            "channel":
            payload["channel"],

            "status":
            status
        }

        try:

            response = requests.post(
                CRM_CALLBACK_URL,
                json=callback_payload
            )

            print(
                "Callback sent:",
                callback_payload
            )

        except Exception as e:

            print(
                "Callback failed:",
                e
            )