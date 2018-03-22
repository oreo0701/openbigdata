# f = open("E:\\python_workspace\\openbigdata\\01_jumptopy\\chap04\\새파일.txt",'r')
# f = open("새파일3.txt",'r')
f = open(".\\새파일4.txt",'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
f.close()

