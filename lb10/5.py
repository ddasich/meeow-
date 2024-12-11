new_line = input("Введите новую строку текста для добавления в файл: ")

with open(r'/Users/m1/Downloads/lab10/file5sss.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

middle_index = len(lines) // 2
lines.insert(middle_index, new_line + "\n")

with open(r'/Users/m1/Downloads/lab10/file5sss.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)

print("Строка успешно добавлена в середину файла.")