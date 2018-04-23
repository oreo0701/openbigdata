

import re

p = re.compile("(9988|7789|7768)")
m = p.sub("####",
"""
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
""")



print(m)
