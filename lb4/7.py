a = input("Введите номер карты:")
dt = [int(d) for d in a]
ch = sum(dt[-1::-2])
n = 0
for d in dt[-2::-2]:
    j = d * 2
    if j > 9:
        j -= 9
    n += j
t = ch + n
if t % 10 == 0:
    print(f"{a} - Правильный номер")
else:
    print(f"{a} - Не правильный номер")

