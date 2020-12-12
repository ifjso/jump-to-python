s = input('input: ')
inputted_numbers  = s.split(' ')

result = [];
for numbers in inputted_numbers:
    existed_numbers = {}
    existed = True

    if len(numbers) < 10:
        existed = False
    else:
        for n in numbers:
            if n in existed_numbers:
               existed = False
               break
            existed_numbers[n] = n

    result.append(existed)

print(result)

