import re

p = re.compile('.*[@].*[.](?=com$|net$).*$')

print(p.match('park@naver.com'))
print(p.match('kim@daum.net'))
print(p.match('lee@myhome.co.kr'))

