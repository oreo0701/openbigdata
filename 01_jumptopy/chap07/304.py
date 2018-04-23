import re
p=re.compile('[a-z]+')
m = p.match("python") #match
m = p.match("3 python") #unmatch

m = p.search("python") #match
m = p.search("3 python") #unmatch
print(m)

result = p.findall("life is too short") #모든 단어가 매치
result = p.search("life is too short") #life만 match
result = p.match("life is too short") #life만 매치
print(result)

result1 = p.finditer("life is too short")
for r in result1: print(r)
print(result1)

