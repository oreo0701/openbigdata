#coding: cp949
x=0
y=0
z=0
print("x: "+str(x)+" y: "+str(y)+" z: "+str(z))     #z를 출력할 수 있도록 포맷스트링으로 변경
input_str="x: {0}, y: {1}, z: {2}".format(x,y,z)
print(input_str)
print("x: {0},y: {1}, z: {2}".format(x,y,z))

if x or y:
    print("if x or y: 조건 만족")
else: 
    print("if x or y: 조건 불만족")

if x and y:
    print("if x and y: 조건 만족")
else:
    print("if x and y: 조건 불만족")

if not x:
    print("if not x: 조건 만족")
else:
    print("if not x: 조건 불만족")

if not y:
    print("if not y: 조건 만족")
else:
    print("if not y: 조건 불만족")

if x and y and z: #아래 조건이 만족할 수 있는 x, y, z 값을 변경할 것
    print("if x and y and z: 조건 만족")
else:    
    print("if x and y and z: 조건 불만족")

if x or y or z:
    print("if x or y or z: 조건 만족")
else:    
    print("if x or y or z: 조건 불만족")

