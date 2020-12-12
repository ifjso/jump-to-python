s = input('input: ')
inputtedNumbers  = s.split(' ')

result = [];
for numbers in inputtedNumbers:
    existedNumbers = {}
    existed = True

    if len(numbers) < 10:
        existed = False
    else:
        for n in numbers:
            if n in existedNumbers:
               existed = False
               break
            existedNumbers[n] = n

    result.append(existed)

print(result)

