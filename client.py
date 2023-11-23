import socket
import ast

def main():
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 1313))

        # 처음 실행 시 로그인 또는 회원가입 선택
        print("1. 로그인\n2. 회원가입\n3. 종료")
        choice = input("선택: ")
        client.send(choice.encode())

        if choice == '1':
            # 로그인
            print(client.recv(1024).decode(), end="")  # "Enter your user_id: "
            user_id = input()
            client.send(user_id.encode())
            print(client.recv(1024).decode(), end="")  # "Enter your user_pw: "
            user_pw = input()

            print(f"[*] Sent user_id: {user_id}, user_pw: {user_pw}")

            login_data = {'user_id': user_id, 'user_pw': user_pw}
            client.send(str(login_data).encode())
            print(client.recv(1024).decode())  # Login result

        elif choice == '2':
            # 회원가입
            user_data = {
                'name': input("Enter your name: "),
                'age': input("Enter your age: "),
                'school': input("Enter your school: "),
                'department': input("Enter your department: "),
                'intro': input("Enter your introduction: "),
                'user_id': input("Enter your user_id: "),
                'user_pw': input("Enter your user_pw: ")
            }
            client.send(str(user_data).encode())
            print(client.recv(1024).decode())  # Registration result

        elif choice == '3':
            print("프로그램을 종료합니다.")
            break

        client.close()

if __name__ == "__main__":
    main()
