a = input("Введите предложение: ")
b = a.split()
res = ""

p = ""
for word in b:
    if word != p:
        if res:
            res += " "
        res += word
    p = word

print("Исправленное предложение:", res)
