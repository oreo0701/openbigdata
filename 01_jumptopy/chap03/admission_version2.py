#coding: cp949

print("�뱸 IT���� ����� ��� ���α׷� Ver. 2\n")
age=0
admission=0
preschool= "����"
youth="���"
teenager="û�ҳ�"
adult="����"
senior="����"

free="����"
two_thousand=2000
three_thousand=3000
five_thousand=5000

output_msg="���̸� �Է��ϼ���: "
output_fee="����� �Է��ϼ���: "


while True:
    print(output_msg, end='')
    customer_input = int (input())
    if customer_input >=0 and customer_input <= 3:
        print("������ ����� %s�̸� ������ %s�Դϴ�." %(preschool,free))
        break

    elif customer_input >= 4 and customer_input <= 13:
        print("������ ����� %s�̸� ����� %d���Դϴ�." %(youth,two_thousand))
        break

    elif customer_input >= 14 and customer_input <= 18:
        print("������ ����� %s�̸� ����� %d���Դϴ�." %(teenager,three_thousand))
        break

    elif customer_input >=19 and customer_input <= 65:
        print("������ ����� %s�̸� ����� %d���Դϴ�." %(adult,five_thousand))
        break

    elif customer_input >= 65:
        print("������ ����� %s�̸� ������ %s�Դϴ�." %(senior,free))
        break

    elif customer_input < 0:
        print("�ٽ� �Է��� �ּ���.\n")
        continue

   
 #       while True:
  #          print(output_fee, end='')
   #         customer_payment = int (input())
    #            if customer_payment < 

