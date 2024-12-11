a = list(input("Введите количество запроосов: "))
if a.count("Q")  > a.count("A"):
    print("-")
elif a.count("Q")  == a.count("A"):
    print("+")
else:
    print("-")