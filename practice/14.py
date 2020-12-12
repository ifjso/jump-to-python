chars = input()

def zip_chars(s):
    count = 0
    temp = ''
    result = ''
    
    for c in s:
        if c != temp:
            temp = c
            if count:
                result += str(count)
            result += c
            count = 1
        else:
            count += 1
    
    if count:
        result += str(count)
    
    return ''.join(result)

print(zip_chars(chars))
