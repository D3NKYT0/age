

def write(email: str, message: str):
    with open('log.txt', mode='w') as email_file:
        content = f'Email: {email} - Msg: {message}'
        email_file.write(content)
