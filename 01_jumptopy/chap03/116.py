#coding: cp949
x=0
y=0
z=0
print("x: "+str(x)+" y: "+str(y)+" z: "+str(z))     #z�� ����� �� �ֵ��� ���˽�Ʈ������ ����
input_str="x: {0}, y: {1}, z: {2}".format(x,y,z)
print(input_str)
print("x: {0},y: {1}, z: {2}".format(x,y,z))

if x or y:
    print("if x or y: ���� ����")
else: 
    print("if x or y: ���� �Ҹ���")

if x and y:
    print("if x and y: ���� ����")
else:
    print("if x and y: ���� �Ҹ���")

if not x:
    print("if not x: ���� ����")
else:
    print("if not x: ���� �Ҹ���")

if not y:
    print("if not y: ���� ����")
else:
    print("if not y: ���� �Ҹ���")

if x and y and z: #�Ʒ� ������ ������ �� �ִ� x, y, z ���� ������ ��
    print("if x and y and z: ���� ����")
else:    
    print("if x and y and z: ���� �Ҹ���")

if x or y or z:
    print("if x or y or z: ���� ����")
else:    
    print("if x or y or z: ���� �Ҹ���")

