def login(users, username, password):
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False