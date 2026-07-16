def login_with_email(email, password, users):
    stored_password = users.get(email)
    if stored_password is None:
        return False
    return stored_password == password
