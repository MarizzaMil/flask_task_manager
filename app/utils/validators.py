import re


def validate_email_password(email, password):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        return False
    if len(password) < 6:
        return False
    return True
