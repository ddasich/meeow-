a = int(input("Введите размер матрицы (n*n):\n"))
m = []
strk = []
for i in range(a):
    strk = []
    for j in range(a):
        chislo = int(input("Введите один элемент матрицы:\n"))
        strk.append(chislo)
    m.append(strk)
print("Матрица:")
for strk in m:
    print(" ".join(map(str, strk)))
print("Измененная матрица(диагонали):")
for i in range(a):
    m[i][i], m[a - 1 - i][i] = m[a - 1 - i][i], m[i][i]

for strk in m:
    print(" ".join(map(str, strk)))