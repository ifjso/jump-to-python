MORSE_RULES = {
    '.-': 'A',	 '-.': 'N',
    '-...': 'B', '---': 'O',
    '-.-.': 'C', '.--.': 'P',
    '-..': 'D',	 '--.-': 'Q',
    '.': 'E',    '.-.': 'R',
    '..-.': 'F', '...': 'S',
    '--.': 'G',	 '-': 'T',
    '....': 'H', '..-': 'U',
    '..': 'I',   '...-': 'V',
    '.---': 'J', '.--': 'W',
    '-.-': 'K',  '-..-': 'X',
    '.-..': 'L', '-.--': 'Y',
    '--': 'M',   '--..': 'Z' }

def morse(s):
    result = []

    words = s.split('  ')
    for word in words:
        chars = word.split(' ')
        for char in chars:
            result.append(MORSE_RULES[char])
        result.append(' ')

    return ''.join(result)

inputted_morse = input('input: ')

print(morse(inputted_morse))

