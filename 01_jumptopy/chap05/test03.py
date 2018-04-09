
def read_content():
    print("<현재 누적 응답 현황>")
    try:
        f = open(".\\poll.txt","r", encoding='UTF8')
        data = f.read()
        print(data)
    except: pass

    choice =input("poll.txt파일을 찾을 수 없습니다. 아래 중 선택하세요.\n"
           "1. 종료 2.새로운 파일생성 3.변경된 파일 경로 입력: ")
    if choice == '1':
        print("프로그램을 종료합니다.")
    elif choice == '2':
        while True:
            survey=input("프로그램이 왜 좋으세요?(\"종료\" 입력시 프로그램 종료): ")
            if survey == "종료":
                print("프로그램을 종료합니다.")
            elif survey != "종료":
                name = input("이름을 입력해주세요: ")
                result = f'[{name}] {survey}'
                f = open(".\\new_poll.txt","w",encoding='UTF8')
                f.write(result)

read_content()