#coding: cp949


age=0
admission=0

output_msg="나이를 입력하세요: "

while True:
    print(output_msg, end='')
    customer_input = int (input())
    if customer_input >=0 and customer_input <= 3:
        print("입장이 무료입니다.")
        break

    elif customer_input >= 4 and customer_input <= 13:
        print("요금은 2000원입니다.")
        break

    elif customer_input >= 14 and customer_input <= 18:
        print("요금은 3000원입니다.")
        break

    elif customer_input >=19 and customer_input <= 65:
        print("요금은 5000원입니다.")
        break

    elif customer_input >= 65:
        print("입장이 무료입니다.")
        break

    else:
        break
    
