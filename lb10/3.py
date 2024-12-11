count = 0
total = 0
letter = "e"

with open(r'/Users/m1/Downloads/lab10/file6.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    words = text.split()
    total = len(words)

    for word in words:
        if letter in word.lower():
            count += 1

if total > 0:
    percentage = count / total * 100
else:
    percentage = 0.0

print("Общее количество слов:", total)
print("Количество слов, в которых есть буква 'e':", count)
print(f"Процент слов с буквой 'e': {percentage:.2f} %")