import os

def search(dirname):
    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.py':
                print('%s/%s' % (path, filename))

search('/jump-to-python')
