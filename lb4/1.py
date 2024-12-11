x = [1,"a",3,4,"b",6]
y = [x[0],x[2],x[3],x[5]]
z = [x[1], x[4]]
del(x)
print(*y)
print(*z)
