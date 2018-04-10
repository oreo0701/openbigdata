
def read_content():
    print("<현재 누적 응답 현황>")
    try:

        f = open(".\\poll.txt","r", encoding='UTF8')
        data = f.read()
        print(data)
    except FileNotFoundError as e:
        choice =input("poll.txt파일을 찾을 수 없습니다. 아래 중 선택하세요.\n"
           "1. 종료 2.새로운 파일생성 3.변경된 파일 경로 입력: ")
        while True:
            if choice == '1':
                print("프로그램을 종료합니다.")
                break
            elif choice == '2':
                survey=input("\n프로그램이 왜 좋으세요?(\"종료\" 입력시 프로그램 종료): ")
                if survey == "종료":
                    print("설문에 응답해 주셔서 감사합니다.")
                    break
                elif survey != "종료":
                    name = input("이름을 입력해주세요: ")
                    result = f'[{name}] {survey}\n'
                f = open(".\\poll.txt","a",encoding='UTF8')
                f.write(result)
                f.close()
                f = open(".\\poll.txt","r",encoding='UTF8')
                two_result=f.read()
                print("<현재 누적 응답 현황>")
                print(two_result)
                f.close()
            elif choice == '3':
                new_file_address = input("변경된 파일 경로를 입력하세요: ")
                f = open(f".\\{new_file_address}\\poll.txt", "r", encoding='UTF8')
                three_result = f.read()
                print("<현재 누적 응답 현황>")
                print(three_result)
                f.close()
                while True:
                    survey = input("프로그램이 왜 좋으세요?(\"종료\" 입력시 프로그램 종료): ")
                    if survey == "종료":
                        print("설문에 응답해 주셔서 감사합니다.")
                        break
                    elif survey != "종료":
                        name = input("이름을 입력해주세요: ")
                        result = f'[{name}] {survey}\n'
                    f = open(f".\\{new_file_address}\\poll.txt", "a", encoding='UTF8')
                    f.write(result)
                    f.close()
                break

read_content()