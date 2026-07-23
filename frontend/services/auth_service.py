import requests

from frontend.services.api import BASE_URL
from frontend.utils.session import save_token


def login(email: str, password: str):

    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": email,
            "password": password
        }
    )

    if response.status_code != 200:
        return None

    data = response.json()

    save_token(data["access_token"])

    return data


def register(
    username: str,
    email: str,
    password: str
):

    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={
            "username": username,
            "email": email,
            "password": password
        }
    )

    return response