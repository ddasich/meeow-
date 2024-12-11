import random
from random import randint

mat = []
n = int(input("Введите количество строк(рядов):"))
m = int(input("Введите количество столбцов(мест):"))
kol = int(input("Введите количество людей в группе:"))
for i in range(n):
    strk = [randint(0,1) for j in range(m)]
    mat.append(strk)


for k in range(n):
    print(*mat[k])
res = 0
for i in range(n):
    f = 0
    for s in mat[i]:
        if s == 0:
            f += 1  #Увеличивается счетчик, если есть место
            if f == kol:
                res = i + 1  #Номер ряда (начиная с первого)
                break
        else:
            e = 0  # Сбрасываем счетчик при встрече с заполненным местом
    if res > 0:
        break  # Прерываем цикл, если нашли нужный ряд


if res > 0:
    print(f"Группа может сесть в ряду номер {res}.")
else:
    print("Нет подходящего ряда.")
