from authentication.login import login
from authentication.signup import signup
from authentication.user import User
from utils.validations import validate_username, validate_password
import json

def load_users():
    try:
        with open("data/users.json", "r") as file:
            users_data = json.load(file)
        users = [User(username, data["password"]) for username, data in users_data.items()]
    except FileNotFoundError:
        users = []
    return users

def save_users(users):
    users_data = {user.username: {"password": user.password} for user in users}
    with open("data/users.json", "w") as file:
        json.dump(users_data, file, indent=2)

def main():
    users = load_users()

    while True:
        print("\n1. Login\n2. Signup\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if login(users, username, password):
                print("Login successful!")
            else:
                print("Invalid username or password.")

        elif choice == "2":
            username = input("Enter a new username: ")
            while not validate_username(username, users):
                print("Username already exists. Choose another one.")
                username = input("Enter a new username: ")

            password = input("Enter a password: ")
            while not validate_password(password):
                print("Password should be at least 6 characters long.")
                password = input("Enter a password: ")

            user = User(username, password)
            users.append(user)
            save_users(users)
            print("Signup successful!")

        elif choice == "3":
            save_users(users)
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()