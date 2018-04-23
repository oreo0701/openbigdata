

import re

p = re.compile("[a-z]+")
m = p.search("5 python")

print(m)
print(m.start()+m.end())