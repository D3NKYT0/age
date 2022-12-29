from time import time

def add_create_at_timestamp(data: object) -> object:
    data.create_at = time()
    return data
