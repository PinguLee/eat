import socket
import threading
import ast

def register_user(data):
    with open('database.txt', 'a') as f:
        f.write(data + '\n')

def login_user(user_id, user_pw):
    with open('database.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            user_data = ast.literal_eval(line.strip())
            if user_data['user_id'] == user_id and user_data['user_pw'] == user_pw:
                return True
    return False

def handle_client(client_socket):
    # 처음 실행 시 로그인 또는 회원가입 선택
    choice = client_socket.recv(1024).decode()
# server.py
    if choice == '1':
        # 로그인
        client_socket.send("Enter your user_id: ".encode())
        user_id = client_socket.recv(1024).decode()
        client_socket.send("Enter your user_pw: ".encode())
        user_pw = client_socket.recv(1024).decode()

        print(f"[*] Received user_id: {user_id}, user_pw: {user_pw}")

        if login_user(user_id, user_pw):
            print("Login successful!")
            client_socket.send("Login successful!".encode())
        else:
            print("Login failed. Invalid user_id or user_pw.")
            client_socket.send("Login failed. Invalid user_id or user_pw.".encode())

    elif choice == '2':
        # 회원가입
        user_data_str = client_socket.recv(1024).decode()
        user_data = ast.literal_eval(user_data_str)
        register_user(str(user_data))
        client_socket.send("Registration successful!".encode())

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 1313))
    server.listen(5)

    print("[*] Listening for connections on 127.0.0.1:12345")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
