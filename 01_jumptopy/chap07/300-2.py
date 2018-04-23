import re

p = re.compile('ca*t')   #* 반복
m = p.match("ct") #match
m = p.match("cat") #match
m = p.match("caaaaat") #match


p = re.compile('ca+t')   #+ 최소 1번 이상 반복
m = p.match("ct") #unmatch
m = p.match("cat") #match
m = p.match("caaaaat") #match


p=re.compile('ab?c') #b가 0~1번 사용되면 매치
m1 = p.match("abc")  #match
m2 = p.match("ac") #match

print(m1)
print(m2)

