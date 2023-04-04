import secrets


def get_random_token():
    token = secrets.token_hex(16)
    return token
