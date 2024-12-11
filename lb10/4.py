

with open(r'/Users/m1/Downloads/lab10/file7.txt', 'r', encoding='utf-8') as file:
    female = []
    for line in file:
        parts = line.split()
        if parts:
            female.append(parts[0])

with open(r'/Users/m1/Downloads/lab10/file8.txt', 'r', encoding='utf-8') as file:
    male = []
    for line in file:
        parts = line.split()
        if parts:
            male.append(parts[0])

try:

    n = int(input("Введите количество имен: "))
    gender = input("Введите пол (м - мужские, ж - женские): ").strip().lower()


    if gender == 'м':
        selected = male[:n]
    elif gender == 'ж':
        selected = female[:n]
    else:
        print("Некорректный ввод пола. Введите 'м' или 'ж'.")
        selected = []


    if selected:
        for name in selected:
            print(name)
    else:
        print("Нет данных для вывода.")

except ValueError:
    print("Ошибка ввода! Убедитесь, что количество имен - это число.")