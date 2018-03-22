# f = open("E:\\python_workspace\\openbigdata\\01_jumptopy\\chap04\\새파일.txt",'r')
# f = open("새파일3.txt",'r')
f = open("..\\relative_path\\dep2\\새파일3.txt",'r')
#.. 은 상위 디렉토리를 말함/ .은 현재 163_3.py가 있는 디렉토리를 말함
line = f.readline()
print(line)
f.close()