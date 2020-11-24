# 04-exercise.py

# Q1
def is_odd(num):
    return num % 2 == 1
print('Q1 %d=%s %d=%s' % (2, is_odd(2), 3, is_odd(3)))

# Q2
def calc_average(*values):
    sum = 0
    for v in values:
        sum += v
    return sum / len(values)
print('Q2 1,2,3,4=%f' % calc_average(1,2,3,4))

# Q5
with open('test.txt', 'w') as f1:
    f1.write('Life is too short')

with open('test.txt', 'r') as f2:
    print('Q5', f2.read())

# Q6
message = input('input:')
with open('test.txt', 'a') as f:
    f.write(message)

# Q7
with open('test.txt', 'r') as f:
    message = f.read()

with open('test.txt', 'w') as f:
    f.write(message.replace('java', 'python'))
