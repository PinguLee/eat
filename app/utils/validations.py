def validate_username(username, existing_users):
    return username not in [user.username for user in existing_users]

def validate_password(password):
    return len(password) >= 6