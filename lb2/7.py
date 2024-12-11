import random
a = int(input("Создаем пароль\nВведите длину:\n "))
b = input("Нужны ли заглавные буквы?\n")
c = input("Нужны ли строчные буквы?\n")
d = input("Нужны ли цифры?\n")
e = input("Нужны ли специальные символы?\n")
pas = " "
ul = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ll = "abcdefghijklmnopqrstuvwxyz"
j = "0123456789"
sc = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
ch = ''

if b == "Да" or b == "да":
    ch += ul
if   c == "Да" or c == "да":
    ch += ll
if  d == "Да" or d == "да":
    ch += j
if    e == "Да" or e == "да":
    ch += sc
else:
        if a == b == c == d == e == "нет" or "Нет":
            print("Не будет вам пароля:0")
for i in range(a):
    pas += random.choice(ch)
print("Ваш пароль", pas)