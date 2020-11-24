# writedata.py

with open('/Users/jso/dev/work-python/jump-to-python/새파일.txt', 'w') as f:
    for i in range(1, 11):
        data = '%d번째 줄입니다.\n' % i
        f.write(data)

