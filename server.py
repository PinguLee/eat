import socket

def main():
    # 서버 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(1)

    # 서버 실행 중임을 알림
    print("서버 실행 중")

    # 클라이언트 연결 대기
    connection, address = server_socket.accept()

    # 클라이언트로부터 데이터 수신
    data = connection.recv(1024)

    # 데이터 처리
    option = data.decode("utf-8")

    # 로그인
    if option == "1":
        login(connection)

    # 회원가입
    elif option == "2":
        register(connection)

    # 종료
    else:
        print("종료합니다.")
        connection.close()
        server_socket.close()
        sys.exit()

def login(connection):
    # ID 입력
    id = connection.recv(1024).decode("utf-8")

    # 데이터베이스에서 ID 검색
    with open("database.txt", "r") as f:
        for line in f:
            if line.split("|")[0] == id:
                # ID가 존재하면 PW 입력받기
                password = connection.recv(1024).decode("utf-8")

                # PW도 일치하면 로그인 성공
                if line.split("|")[1] == password:
                    # 회원 정보 출력
                    connection.sendall("로그인 성공!")
                    name = line.split("|")[2]
                    age = line.split("|")[3]
                    school = line.split("|")[4]
                    department = line.split("|")[5]
                    self_introduction = line.split("|")[6]
                    connection.sendall(f"{name}|{age}|{school}|{department}|{self_introduction}".encode("utf-8"))
                    return

    # ID가 존재하지 않으면 로그인 실패
    connection.sendall("존재하지 않는 ID입니다.")

def register(connection):
    # 회원 정보 입력
    name = connection.recv(1024).decode("utf-8")
    age = connection.recv(1024).decode("utf-8")
    school = connection.recv(1024).decode("utf-8")
    department = connection.recv(1024).decode("utf-8")
    self_introduction = connection.recv(1024).decode("utf-8")
    id = connection.recv(1024).decode("utf-8")
    password = connection.recv(1024).decode("utf-8")

    # 데이터베이스에 회원 정보 저장
    with open("database.txt", "a") as f:
        f.write(f"{name}|{age}|{school}|{department}|{self_introduction}|{id}|{password}\n")

    connection.sendall("회원가입 성공!")

if __name__ == "__main__":
    main()
