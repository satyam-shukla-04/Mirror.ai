BASE_URL = "http://127.0.0.1:8000"

def get_headers(token=None):

    headers = {}

    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers