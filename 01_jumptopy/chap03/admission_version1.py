#coding: cp949


age=0
admission=0

output_msg="���̸� �Է��ϼ���: "

while True:
    print(output_msg, end='')
    customer_input = int (input())
    if customer_input >=0 and customer_input <= 3:
        print("������ �����Դϴ�.")
        break

    elif customer_input >= 4 and customer_input <= 13:
        print("����� 2000���Դϴ�.")
        break

    elif customer_input >= 14 and customer_input <= 18:
        print("����� 3000���Դϴ�.")
        break

    elif customer_input >=19 and customer_input <= 65:
        print("����� 5000���Դϴ�.")
        break

    elif customer_input >= 65:
        print("������ �����Դϴ�.")
        break

    else:
        break
    
