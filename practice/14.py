chars = input()

def zip_chars(s):
    i = 1
    count = 1
    temp = s[0]
    result = []
    
    while i < len(s):
        if temp == s[i]:
            count += 1
        else:
            result.append(temp)
            result.append(str(count))
            count = 1
        temp = s[i]
        i += 1

    result.append(temp)
    result.append(str(count))
    
    return ''.join(result)

print(zip_chars(chars))
