import os

print(os.getcwd())

print(os.chdir('..\\..\\.\\'))
print(os.getcwd())

print(os.chdir('c:\WINDOWS'))
print(os.getcwd())
os.system('dir > windows_file_list.txt')
os.system('notepad windows_file_list.txt')

f = os.popen("dir")
f.readlines()