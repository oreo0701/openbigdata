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
        age =0
        admission=0
    

    elif customer_input >= 4 and customer_input <= 13:
        print("������ ����� %s�̸� ����� %d���Դϴ�." %(youth,two_thousand))
        age =4
        admission=2000
        

    elif customer_input >= 14 and customer_input <= 18:
        print("������ ����� %s�̸� ����� %d���Դϴ�." %(teenager,three_thousand))
        age=14
        admission=3000
        

    elif customer_input >=19 and customer_input <= 65:
        print("������ ����� %s�̸� ����� %d���Դϴ�." %(adult,five_thousand))
        age=19
        admission=5000
        

    elif customer_input >= 65:
        print("������ ����� %s�̸� ������ %s�Դϴ�." %(senior,free))
        age=65
        admission=0
        
    elif customer_input < 0:
        print("�ٽ� �Է��� �ּ���.\n")
        continue

    while age > 0 and age < 65:
        print(output_fee, end='')
        customer_payment = int (input())
        if customer_payment == admission:
            print("�����մϴ�. Ƽ���� �����մϴ�.")
            break

        elif customer_payment < admission:
            print("%d���� ���ڶ��ϴ�. �����Ͻ� %d���� ��ȯ�մϴ�." 
                %(admission-customer_payment, customer_payment))
            break
        elif customer_payment > admission:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�." 
                %(customer_payment-admission))
            break
        
        else:
            break
   
      
    break

