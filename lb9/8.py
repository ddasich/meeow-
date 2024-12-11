# Ввод размеров матрицы
a = int(input("Введите количество строк (a): "))
b = int(input("Введите количество столбцов (b): "))

# Создаем пустую матрицу
matrix = [[0] * b for _ in range(a)]

# Заполненяем матрицу
for i in range(a): #ряд
    for j in range(b): #столбец
        if i == 0 or j == 0:
            matrix[i][j] = 1
        else:
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

# Вывод матрицы
print("Сформированная матрица:")
for row in matrix:
    print(" ".join(f"{elem:6}" for elem in row))
