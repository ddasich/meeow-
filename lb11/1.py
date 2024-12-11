keypad = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' '
}

input_text = input("Введите слово или фразу: ").upper()

result = ""

for char in input_text:
    for num, letters in keypad.items():
        if char in letters:
            presses = letters.index(char) + 1
            result += num * presses
            break

print(result)