import re

p=re.compile('[a-c]')

m = p.match("able")
m = p.match("Able")  #unmatch 대소문자 구분

p = re.compile('[0-9]')
m = p.match('a9')  #unmatch
m = p.match('9a')  #match
m = p.match('9a;dkjfs;jdfskjsf') #still match


p=re.compile('[a-zA-Z]') #대소문자 구분하지 않고 매치
print(m)
