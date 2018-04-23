import re
p =re.compile('Crow|Servo')
m=p.match('CrowHello')
m=p.match('Servo')

print(m)

p=re.compile('short$')
m1 = p.search('Life is too short')

print(m1)