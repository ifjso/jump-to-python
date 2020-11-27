# 03-exercise.py

# Q2
num = 0
result = 0
while num < 1000:
    num += 1
    if num % 3 == 0:
        result += num
print('Q2', result)

# Q3
print('Q3')
num = 0
while num < 5:
    num += 1
    print('*' * num)

# Q4
print('Q4')
for i in range(1, 101):
    print(i, end=" ")
print()

# Q5
scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in scores:
    total += score
print('Q5', total / len(scores))

# Q6
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print('Q6', result)
