pts = {
    '1': ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
    '2': ['D', 'G'],
    '3': ['B', 'C', 'M', 'P'],
    '4': ['F', 'H', 'V', 'W', 'Y'],
    '5': ['K'],
    '8': ['J', 'X'],
    '10': ['Q', 'Z']
}

w = input("Ну же, вводи уже слово:")
w = w.upper()
total = 0

for letter in w:
    for val, chars in pts.items():
        if letter in chars:
            total += int(val)

print(f"Это вот, чо стоит твоё слово: {total}")