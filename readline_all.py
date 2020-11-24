# readline_all.py

with open('/Users/jso/dev/work-python/jump-to-python/새파일.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)

with open('/Users/jso/dev/work-python/jump-to-python/새파일.txt', 'r') as f:
    data = f.read()
    print(data)

