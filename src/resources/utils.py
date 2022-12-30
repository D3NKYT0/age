import datetime

def add_create_at_timestamp(data: object) -> object:
    data.create_at = datetime.datetime.utcnow().astimezone().isoformat()
    return data
