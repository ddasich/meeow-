a = input("Введите 1 слово для замены:")
b = input("Введите 2 слово для замены:")
c = input("Введите 3 слово для замены:")

for w in [a, b, c]:
    if len(w) < 10:
        print(w)
    else:
        aw = f"{w[0]}{len(w) - 2}{w[-1]}"
        print(aw)

