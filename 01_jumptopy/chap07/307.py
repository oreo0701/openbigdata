import re
p=re.compile('[a-z]+')

# m = p.match("python")
m = p.search("3 python")
print(m)
print(m.start())
print(m.end())
print(m.span())

