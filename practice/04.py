A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
while A:
    score = A.pop()
    if score >= 50:
        sum += score

print(sum)

