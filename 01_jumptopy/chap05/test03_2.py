file_name='\\poll.txt'
path='.'

def read_content():
    f=open(f"{path}{file_name}","r", encoding='UTF8')
    data = f.read()
    print(data)
    f.close()

try:
    read_content()
except FileNotFoundError:
    choice = input("poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.\n1.종료 2. 새로운 파일생성 3.변경된 파일 경로 입력: ")
    if choice == '1':
        print("설문에 응답해 주셔서 감사합니다.")
    elif choice == '2':
        pass
    elif choice == '3':
        path = input("변경된 파일 경로를 입력하세요: ")

while True:
    try:
        read_content()
    except:
        pass
    survey = input("\n프로그램이 왜 좋으세요?(\'종료\'입력시 프로그램 종료): ")
    if survey == '종료':
        print("설문에 응답해 주셔서 감사합니다.")
        break
    else:
        name = input("이름을 입력하세요: ")
        f = open(f"{path}{file_name}","a", encoding='UTF8')
        result = f'[{name}] {survey}\n'
        f.write(result)
        f.close()

