with open(r'/Users/m1/Downloads/lab10/file5.txt', encoding='utf-8') as file:
    a = file.read()
    if "Academy" in a:
        print("В 5 файле есть слово Academy")
        file.close()
    else:
        file.close()
with open(r'/Users/m1/Downloads/lab10/file6.txt', encoding='utf-8') as file:
    a = file.read()
    if "Academy" in a:
        print("В 6 файле есть слово Academy")
        file.close()
    else:
        file.close()
