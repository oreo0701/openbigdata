#coding: cp949

print("\n<�뱸 IT���� ����� ��� ���α׷� Ver. 5>\n")
age=0
admission=0
customer_num =0
free_ticket=3
annual_membership=5

preschool= "����"
youth="���"
teenager="û�ҳ�"
adult="����"
senior="����"

free="����"
two_thousand=2000
three_thousand=3000
five_thousand=5000
card=admission*0.9

while True:
    customer_num +=1
    print("--------------------")
    print("%d��° �մ��̽ʴϴ�."%customer_num)
    customer_input = int (input("\n���̸� �Է��ϼ���: "))
    if customer_input >=0 and customer_input <= 3:
        print("������ ����� %s�̸� ������ %s�Դϴ�.\n" %(preschool,free))
        admission=0
        continue 
    elif customer_input >= 4 and customer_input <= 13:
        print("������ ����� %s�̸� ����� %d���Դϴ�.\n" %(youth,two_thousand))
        admission=2000
        age=4
    
    elif customer_input >= 14 and customer_input <= 18:
        print("������ ����� %s�̸� ����� %d���Դϴ�.\n" %(teenager,three_thousand))
        admission=3000
        age=14       
    
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
        continue          
    elif customer_input < 0:
        print("�ٽ� �Է��� �ּ���.\n")
        continue
  
    customer_option = int(input("��� ������ �����ϼ���. (1: ����, 2:���� ���� �ſ�ī��): "))


   
    
    if customer_option ==1:
        customer_payment = int(input("����� �Է��ϼ���: "))
        
        if customer_payment >= admission and customer_num %7 == 0 and free_tickcet > 0: 
            free_ticket -=1
            print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d\n" %free_ticket)
        elif customer_payment >= admission and customer_num %4 == 0 and annual_membership > 0:
            annual_membership -=1
            print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d\n" %annual_membership)
        
        if customer_payment == admission:
            print("�����մϴ�. Ƽ���� �����մϴ�.\n")
        elif customer_payment < admission:
            print("%d���� ���ڶ��ϴ�. �����Ͻ� %d���� ��ȯ�մϴ�.\n" %(admission-customer_payment, customer_payment))
        elif customer_payment > admission:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�.\n"%(customer_payment-admission))
    
    elif customer_option ==2:
        if age < 60:
            print("Ƽ���� �����ϰ� ����ݾ׿� 10%%�� ���ε� %d���� �����˴ϴ�.\n"%(card))
            card=admission*0.9
        else :
            card=card*0.95
            print("Ƽ���� �����ϰ� ����� 5%% �߰������� ����� %d���� �����˴ϴ�."%(card))
                
        if customer_num %7 == 0 and free_ticket > 0:
            free_ticket -=1
            print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d\n" %free_ticket)
        elif customer_num %4 == 0 and annual_membership > 0:
            annual_membership -=1
            print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d\n" %annual_membership) 
            
         

        
        
      

