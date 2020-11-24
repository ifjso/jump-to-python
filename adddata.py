# adddata.py

with open('/Users/jso/dev/work-python/jump-to-python/새파일.txt', 'a') as f:
    for i in range(11, 20):
        data = '%d번째 줄입니다.\n' % i
        f.write(data)

