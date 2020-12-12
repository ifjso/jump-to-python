s = input('input: ')
inputted_numbers  = s.split(' ')

def check_dup_num(s):
    bucket = []
    
    for n in s:
        if n not in result:
            bucket.append(n)
        else:
            return False

    return len(bucket) == 10

result = []
for numbers in inputted_numbers:
    result.append(check_dup_num(numbers))

print(result)

