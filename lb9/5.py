n, m = map(int, input("Введите размер матрицы(nxn):\n").split())

#Ввод матрицы размером n x m
mat = [list(map(int, input("Введите элементы матрицы(в соответствии с размером): ").split())) for k in range(n)]

#Изменение матрицы
t = [[mat[j][i] for j in range(n)] for i in range(m)]

#Вывод измененной матрицы
for row in t:
    print(*row)
