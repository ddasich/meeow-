import random
from random import randint

t = [
    [1, 2],
    [3, 5],
    [5, 6],
    [7, 8]
]
x = randint(1, 8)
y = randint(1, 8)
print("Количество сокровищ:")
print(len(t))
print("Координаты сокровищ:")
for i in t:
    print(*i)
print("Координаты Александра:")
print(x, y)

d_min = float('inf')
n_treasure = None
for tr in t:
    d_sq = (tr[0] - x) ** 2 + (tr[1] - y) ** 2

    if d_sq < d_min:
        d_min = d_sq
        n_treasure = tr
print("Ближайшее сокровище:")
print(*n_treasure)
