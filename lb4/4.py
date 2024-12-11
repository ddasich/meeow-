a = []
while 1:
    b = input("(Для выхода нажмите Еnter)\nВведите число:")
    if b == "":
        break
    try:
        a.append(int(b))
    except ValueError:
        print("Введите правильное число")

x = sum(a)/len(a)

l = []
m = []

for n in a:
        if n < x:
            l.append(n)
        elif n > x:
            m.append(n)

print("Среднее значение списка:", x)
print(*l)
print(*m)
