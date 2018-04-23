import re


p=re.compile('aaa.bbb')
# dest_str = "aaa|bbb"

dest_str = "aaa\n\n\nbbb"

m = p.match(dest_str) #unmatch


p=re.compile('aaa.bbb',re.DOTALL)
m1 = p.match(dest_str)

print(m)
print(m1)

p=re.compile('[a-z]',re.I)
m2= p.match('python')
m2= p.match('PYTHON')
m2= p.match('Python')
print(m2)