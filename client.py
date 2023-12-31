import sys

def main():
    # 입력 받기
    option = input("1. 로그인 2. 회원가입: ")

    # 로그인
    if option == "1":
        login()

    # 회원가입
    elif option == "2":
        register()

    # 종료
    else:
        print("종료합니다.")
        sys.exit()

def login():
    # ID 입력
    id = input("ID를 입력하세요: ")

    # 데이터베이스에서 ID 검색
    with open("database.txt", "r") as f:
        for line in f:
            if line.split("|")[0] == id:
                # ID가 존재하면 PW 입력받기
                password = input("PW를 입력하세요: ")

                # PW도 일치하면 로그인 성공
                if line.split("|")[1] == password:
                    print("로그인 성공!")
                    return

    # ID가 존재하지 않으면 로그인 실패
    print("존재하지 않는 ID입니다.")

def register():
    # 회원 정보 입력
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    school = input("학교를 입력하세요: ")
    department = input("학과를 입력하세요: ")
    self_introduction = input("자기소개를 입력하세요: ")
    id = input("ID를 입력하세요: ")
    password = input("PW를 입력하세요: ")

    # 데이터베이스에 회원 정보 저장
    with open("database.txt", "a") as f:
        f.write(f"{name}|{age}|{school}|{department}|{self_introduction}|{id}|{password}\n")

    print("회원가입 성공!")

if __name__ == "__main__":
    main()