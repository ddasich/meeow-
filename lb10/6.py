a = (input("Введите 'шифровка' или 'дешифровка': ").lower())
if 'дешифровка' in a:
    with open('/Users/m1/Downloads/lab10/file62sss.txt', 'r', encoding="UTF-8") as f:
        task6 = f.read()

    symbols = task6.split()
    print(symbols)

    rashifr = ""
    for n in range(len(symbols)):
        bukvas = list(symbols[n])
        for x in range(len(bukvas)-1, -1,-1):
            rashifr = rashifr + bukvas[x]
        rashifr = rashifr + " "
    print("Расшифрованный текст: ", rashifr)


elif 'шифровка' in a:
    with open('/Users/m1/Downloads/lab10/file6sss.txt', 'r', encoding="UTF-8") as f:
        task62 = f.read()

    symbols = task62.split()
    print(symbols)

    shifr = ""
    for n in range(len(symbols)):
        bukvas = list(symbols[n])
        for x in range(len(bukvas)-1, -1,-1):
            shifr = shifr + bukvas[x]
        shifr = shifr + " "
    print("Зашифрованный текст: ", shifr)

