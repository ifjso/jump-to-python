# 02-exercise.py

# Q1
avg = (80 + 75 + 55) / 3
print('Q1', avg)

# Q2
isEven = 13 % 2 == 0
print('Q2', isEven)

# Q3
pin = '881120-1068234'
dateOfBirth = pin[:6]
num = pin[7:]
print('Q3', dateOfBirth, num)

# Q4
pin = '881120-1068234'
print('Q4', pin[7])

# Q5
a = "a:b:c:d"
b = a.replace(':', '#')
print('Q5', b)

# Q6
numbers = [1, 3, 5, 4, 2]
numbers.sort()
numbers.reverse()
print('Q6', numbers)

# Q7
l = ['Life', 'is', 'too', 'short']
print('Q7', ' '.join(l))

# Q8
t1 = (1, 2, 3)
t2 = (4,)
print('Q8', t1 + t2)

# Q10
a = {'A':90, 'B':80, 'C':70}
print('Q9', a.pop('B'))

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = list(set(a))
print('Q11', b)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print('Q12', b)
