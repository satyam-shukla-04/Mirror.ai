import requests

from frontend.services.api import (
    BASE_URL,
    get_headers
)

from frontend.utils.session import get_token


def generate_text(prompt: str):

    token = get_token()

    response = requests.post(
        f"{BASE_URL}/generate/text",
        headers=get_headers(token),
        json={
            "prompt": prompt
        }
    )

    return response