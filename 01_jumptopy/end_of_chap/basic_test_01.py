
print("극장 입장권 판매를 시작합니다.\n")

while True:
    try:
        age = int(input("현재 나이를 입력하세요: "))
        if age < 3:
            print("무료 입장입니다.\n")
        elif age >= 3 and age <=12:
            print("입장료는 10달러 입니다.\n")
        elif age >= 13:
            print("입장료는 15달러 입니다.\n")
    except:
        print("다시 입력해주세요.\n")

