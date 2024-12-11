import random
from random import randint

while True:
    m = [[randint(0, 9), randint(0, 9), randint(0, 9)],
         [randint(0, 9), randint(0, 9), randint(0, 9)],
         [randint(0, 9), randint(0, 9), randint(0, 9)]]

    if (m[0][0] + m[0][1] + m[0][2] == m[1][0] + m[1][1] + m[1][2] and
        m[0][0] + m[0][1] + m[0][2] == m[2][0] + m[2][1] + m[2][2] and
        m[0][0] + m[1][1] + m[2][2] == m[0][2] + m[1][1] + m[2][0] and
        m[0][0] + m[1][0] + m[2][0] == m[0][1] + m[1][1] + m[2][1] == m[0][2] + m[1][2] + m[2][2]):
        print("Магический квадрат.")
        print(*m[0])
        print(*m[1])
        print(*m[2])
        break
    else:
        print("Не магический квадрат.")
