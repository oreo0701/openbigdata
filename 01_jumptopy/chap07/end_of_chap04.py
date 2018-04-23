

import re

p = re.compile(".*[@].*[.].*$")

m1 = p.match("park@naver.com")
m2 = p.match("kim@daum.net")
m3 = p.match("lee@myhome.co.kr")

print(m1)
print(m2)
print(m3)
