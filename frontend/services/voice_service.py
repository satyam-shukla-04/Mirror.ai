import requests

from frontend.services.api import (
    BASE_URL,
    get_headers
)

from frontend.utils.session import get_token


def generate_voice(generated_text_id: int):

    print("Generated Text ID:", generated_text_id)

    token = get_token()

    response = requests.post(
        f"{BASE_URL}/voice/generate",
        headers=get_headers(token),
        json={
            "generated_text_id": generated_text_id
        }
    )

    print(response.status_code)
    print(response.text)

    return response