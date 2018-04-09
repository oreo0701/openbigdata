

def compare(num):
    if num % 10 == 0:
        return "True"
    elif num == -1:
        return "프로그램을 종료합니다."
    else:
        return "False"


print("10의 배수인지를 확인하는 함수입니다.\n")
while True:
    num = int(input("양수를 입력하세요(종료: -1): "))
    if num != -1:
        print(compare(num))
    else:
        print("프로그램을 종료합니다.")
        break