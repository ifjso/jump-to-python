def getTotalPage(m, n):
    if m == 0:
        return 0
    return (m - 1) // n + 1

print(getTotalPage(0, 20))
print(getTotalPage(1, 20))
print(getTotalPage(20, 20))
print(getTotalPage(21, 20))
