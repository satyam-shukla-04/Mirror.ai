token = None


def save_token(jwt: str):
    global token
    token = jwt


def get_token():
    return token


def clear_token():
    global token
    token = None