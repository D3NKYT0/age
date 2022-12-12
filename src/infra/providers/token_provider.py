from auth import jose as auth


def generate_access_token(data: dict):
    return auth.cat(data=data)


def verify_access_token(token: str):
    return auth.vat(token)
