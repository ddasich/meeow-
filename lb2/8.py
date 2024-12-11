a =  input("Введите счет матча(Формат: Команда-Команда A:B): \n")
a1 = a.split()
k = a1[0].split('-')
s = a1[1].split(':')
t1 = int(s[0])
t2 = int(s[1])
if t1 > t2:
    print(k[0])
elif t1 < t2:
    print(k[1])
else:    print("У команд: ", k,  "\nНичья!")