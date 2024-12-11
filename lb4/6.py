import random
a = ["O","P"]
c = 0
t = 0
l = None

while c<3:
    b = random.choice(a)
    t +=1
    print(b, end= ' ')

    if b == l:
        c +=1
    else:
        c = 1
    l = b

print("Попыток:",t )