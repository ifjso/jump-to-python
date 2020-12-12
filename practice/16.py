MOS_RULES = {
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

inputted_mos = input('input: ')
words_mos = inputted_mos.split('  ')

result = ''
for word_mos in words_mos:
    alphabets_mos = word_mos.split(' ')
    for alphabet_mos in alphabets_mos:
        result += MOS_RULES[alphabet_mos]
    result += ' '

print(result.strip())

