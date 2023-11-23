def signup(users, username, password):
    from user import User  # 상대 경로로 사용자 모듈 불러오기

    user = User(username, password)
    users.append(user)
    return user