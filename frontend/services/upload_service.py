import requests

from frontend.services.api import (
    BASE_URL,
    get_headers
)

from frontend.utils.session import get_token


def upload_document(file_path: str):

    token = get_token()

    with open(file_path, "rb") as file:

        response = requests.post(
            f"{BASE_URL}/upload/document",
            headers=get_headers(token),
            files={
                "file": file
            }
        )

    return response

def upload_voice(file):
    return requests.post(
        f"{BASE_URL}/upload/voice",
        files={
            "file": (
                file.name,
                file.read(),
                file.type,
            )
        },
    )