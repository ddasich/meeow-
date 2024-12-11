w = input("Введите зашифрованое слово: ")
s1 = " "
s2 = " "
c = 0
if "#" in w:
    w = w.replace("#", "")
else:
    print("Неверно!")

for t in w:
    c += 1
    if (c % 2 == 1):
        s1 += t
    else:
        s2 = t + s2

print("Расшифрованое слово: ", s1 + s2)