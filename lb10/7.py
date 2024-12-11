import random

with open(r'/Users/m1/Downloads/lab10/file7sss.txt', 'r', encoding='utf-8') as file:
    words = [word for word in file.read().split() if len(word) >= 3]  #
    p = ''

    while len(p) < 8 or len(p) > 10:
        word1 = random.choice(words)
        word2 = random.choice(words)
        p = word1.capitalize() + word2.capitalize() 

    print(p)