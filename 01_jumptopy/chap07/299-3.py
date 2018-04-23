import re

# p=re.compile('[0-9]')
p=re.compile('\d')  #숫자와 매치
m = p.match('7') #match

p=re.compile('\D')  #숫자가 아닌것과 매치
m = p.match('s') #match

p=re.compile(' ')  #공백문자와 매치
m = p.match(' ') #match

p=re.compile('\s')  #공백문자와 매치
m = p.match(' ') #match

p=re.compile('\S')  #공백이 아닌것과 매치
m = p.match('S') #match

p=re.compile('[a-zA-Z0-9]')  #문자와 숫자 매치
m = p.match('A') #match

p=re.compile('\w')  #문자와 숫자 매치
m = p.match('A') #match

p=re.compile('\W')  #문자와 숫자가 아닌 것과 매치
m = p.match('!') #match

p=re.compile('[a-z][0-9]-case')
m = p.match('a1-case')


print(m)
