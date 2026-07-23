import requests

from frontend.services.api import (
    BASE_URL,
    get_headers
)

from frontend.utils.session import get_token


def evaluate_text(
    generated_text_id: int
):

    token = get_token()

    response = requests.post(
        f"{BASE_URL}/evaluate/text",
        headers=get_headers(token),
        json={
            "generated_text_id": generated_text_id
        }
    )

    return response


def get_history():

    token = get_token()

    response = requests.get(
        f"{BASE_URL}/evaluate/history",
        headers=get_headers(token)
    )

    return response