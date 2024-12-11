a = input("Введите текст Хайку: ")
b = a.split()
if len (b) < 3 or len(b) > 3:
    print("Не Хайку")
else:
    print("Хайку")