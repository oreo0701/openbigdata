#coding: cp949

#pocket = ['paper', 'cellphone', 'money', 'card']
#pocket = ['paper', 'cellphone']
#pocket = ['paper']
pocket=[]

item=input("���Ͽ� �������� ì�⼼��: ")
#pocket.insert(0,item)  insert�� (�� ��°��, �߰��� ���) 2 argument�� �ʿ�
pocket.append(item)

if 'card' in pocket:
    print("�ſ�ī��� �ýø� Ż ���� ��õ�մϴ�.")
elif 'money' in pocket:
    print("���� �̿�� �������� �� ì�⼼��")
elif 'cellphone' in pocket:
    print("����Ʈ���� ����ī�� ����� �ִ��� Ȯ���ϼ���")
else:
    pass 
