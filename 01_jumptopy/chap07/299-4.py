import re

p=re.compile('a.b')  #. 모든 문자와 매치 \n제외하고
m = p.match('akb') #match
m = p.match('a-b')
m = p.match('a!b')

p=re.compile('330.py')  #. 모든 문자와 매치 \n제외하고
m = p.match('330.py') #match
m = p.match('330_py') #원하는 결과가 아님

p=re.compile('330[.]py')  #. 모든 문자와 매치 \n제외하고
m = p.match('330.py') #match
m = p.match('330_py') #unmatch

print(m)
