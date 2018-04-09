

while True:
    survey=input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료): ")
    if survey == '종료':
        print("프로그램을 종료합니다.")
        break
    elif survey != '종료':
        name=input("이름을 입력해주세요: ")
        print('설문에 응해 주셔서 감사합니다.')
        result= f'[{name}] {survey}\n'
        f = open(".\\poll.txt", "a", encoding='UTF8')
        f.write(result)