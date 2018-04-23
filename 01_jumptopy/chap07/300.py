import re

p = re.compile('ca*t')   #* 반복
m = p.match("ct") #match
m = p.match("cat") #match
m = p.match("caaaaat") #match


p = re.compile('ca+t')   #+ 최소 1번 이상 반복
m = p.match("ct") #unmatch
m = p.match("cat") #match
m = p.match("caaaaat") #match


p=re.compile('.+[.]...')
m1 = p.match("a.txt")
m2 = p.match("bk3.pyy")
m3 = p.match("python.doc")

print(m1)
print(m2)
print(m3)


p=re.compile('ca{2}t') #a가 2번 반복되면 매치
m1 = p.match("cat")#unmatch
m2 = p.match("caat")#match
m3 = p.match("caaaat") #unmatch
print(m1)
print(m2)
print(m3)


p=re.compile('ca{2,5}t') #a가 2~5번 반복되면 매치
m1 = p.match("cat")#unmatch
m2 = p.match("caat")#match
m3 = p.match("caaaaat") #match
print(m1)
print(m2)
print(m3)

