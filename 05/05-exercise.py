# Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print('Q1', cal.value)

# Q2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print('Q2', cal.value)

# Q4
l = [1, -2, 3, -5, 8, -3]
print('Q4', list(filter(lambda n: n > 0, l)))

# Q5
h = hex(234)
print('Q5', int(h, 16))

# Q6
l = [1, 2, 3, 4]
print('Q6', list(map(lambda n: n * 3, l)))

# Q7
l = [-8, 2, 7, 5, -3, 5, 0, 1]
print('Q7', max(l) + min(l))

# Q8
n = 17 / 3
print('Q8', round(n, 4))

# Q9
import sys
print('Q9', sum(map(lambda n: int(n), sys.argv[1:])))

# Q10
import os
os.chdir('/jump-to-python')
f = os.popen('ls')
print('Q10', f.read())

# Q11
import glob
print('Q11', glob.glob('/jump-to-python/05/*.py'))

# Q12
import time
print('Q12', time.strftime('%Y/%m/%d %H:%M:%S'))

# Q13
import random

result = []
while len(result) < 6:
    n = random.randint(1, 45)
    if n not in result:
        result.append(n)

print('Q13', result)
