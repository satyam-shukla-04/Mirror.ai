import requests

from frontend.services.api import (
    BASE_URL,
    get_headers,
)

from frontend.utils.session import get_token


def generate_voice(
    generated_text_id=None,
    custom_text=None,
):

    token = get_token()

    payload = {}

    if generated_text_id is not None:
        payload["generated_text_id"] = generated_text_id

    if custom_text:
        payload["custom_text"] = custom_text

    response = requests.post(
        f"{BASE_URL}/voice/generate",
        headers=get_headers(token),
        json=payload,
    )

    print(response.status_code)
    print(response.text)

    return response


def get_voice_history():

    token = get_token()

    return requests.get(
        f"{BASE_URL}/voice/history",
        headers=get_headers(token),
    )


def get_reference_voice():

    token = get_token()

    return requests.get(
        f"{BASE_URL}/upload/voice/latest",
        headers=get_headers(token),
    )