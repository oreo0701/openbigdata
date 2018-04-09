
while True:
    num = input("세 개의 양수를 입력하세요(종료 -1): ")
    num_list = num.split()
    num1 = num_list[0]
    if num_list[0] == '-1':
        print("프로그램을 종료합니다.")
        break
    elif num_list[0] != -1:
        num2 = num_list[1]
        num3 = num_list[2]

        if int(num3) % int(num1) ==0 and int(num3) % int(num2) == 0:
            print(f"{num3}는 {num1}와 {num2}의 공배수입니다.")
            continue

        else:
            print(f"{num3}는 {num1}와 {num2}의 공배수가 아닙니다.")
