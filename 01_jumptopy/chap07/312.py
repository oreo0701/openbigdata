import re

p=re.compile('\\section')

data="\\section"


m = p.findall("\section")
m1 = p.findall(" section")

p=re.compile("\\section")
m2 = p.matchz("\section")

print(m)
print(m1)
print(m2)