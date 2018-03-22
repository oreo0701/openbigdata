f = open(".\\새파일4.txt",'r')

lines = f.readlines()

for line in lines:
    print(line, end='')
f.close()

