#coding: cp949

print("�뱸 IT���� ����� ��� ���α׷� Ver. 4\n")
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
output_option="��� ������ �����ϼ���. (1: ����, 2:���� ���� �ſ�ī��): "

while True:
    print(output_msg, end='')
    customer_input = int (input())
    if customer_input >=0 and customer_input <= 3:
        print("������ ����� %s�̸� ������ %s�Դϴ�.\n" %(preschool,free))
        age =0
        admission=0
    
    elif customer_input >= 4 and customer_input <= 13:
        print("������ ����� %s�̸� ����� %d���Դϴ�.\n" %(youth,two_thousand))
        age =4
        admission=2000
        
    elif customer_input >= 14 and customer_input <= 18:
        print("������ ����� %s�̸� ����� %d���Դϴ�.\n" %(teenager,three_thousand))
        age=14
        admission=3000
        
    elif customer_input >=19 and customer_input <= 59:
        print("������ ����� %s�̸� ����� %d���Դϴ�.\n" %(adult,five_thousand))
        age=19
        admission=5000
        
    elif customer_input >=60 and customer_input <= 65:
        print("������ ����� %s�̸� ����� %d���Դϴ�.\n" %(adult,five_thousand))
        age=60
        admission=5000

    elif customer_input >= 66:
        print("������ ����� %s�̸� ������ %s�Դϴ�.\n" %(senior,free))
        age=65
        admission=0
        
    elif customer_input < 0:
        print("�ٽ� �Է��� �ּ���.\n")
        continue
    
    while age >0 and age <65 :
        card=admission*0.9
        print(output_option, end='')
        customer_option = int(input())
       
        if customer_option ==1:
            print(output_fee, end='')
            customer_payment = int(input())
            
            if customer_payment == admission:
                print("�����մϴ�. Ƽ���� �����մϴ�.\n")
                break
            elif customer_payment < admission:
                print("%d���� ���ڶ��ϴ�. �����Ͻ� %d���� ��ȯ�մϴ�.\n" 
                %(admission-customer_payment, customer_payment))
                break
            elif customer_payment > admission:
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�.\n" 
                %(customer_payment-admission))
                break
        elif customer_option ==2:
            if age < 60:
                print("Ƽ���� �����ϰ� ����ݾ׿� 10%%�� ���ε� %d���� �����˴ϴ�.\n"%(card))
                card=admission*0.9
                break            
            else :
                card=card*0.95
                print("Ƽ���� �����ϰ� ����� 5%% �߰������� ����� %d���� �����˴ϴ�."
                    %(card))
                break
    break
      

