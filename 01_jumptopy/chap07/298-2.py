import re

p=re.compile('[a-c]-case')
#unmatch
m = p.match("able")
#match
m = p.match("a-case")
m = p.match("b-case")
m = p.match("c-case")
m = p.match("c-casesdsfdsfdfsfd")

print(m)
