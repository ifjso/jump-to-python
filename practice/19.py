import re

s = """park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768"""

p = re.compile('(?P<front>\d+[-]\d+)[-]\d+')

print(p.sub('\g<front>-####', s))

