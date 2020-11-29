f = open('sample.txt', 'r')
lines = f.readlines()
f.close()

sum = 0
for line in lines:
    sum += int(line)

f = open('result.txt', 'w')
f.write(str(sum / len(lines)))
f.close()
