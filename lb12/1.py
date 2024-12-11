n = int(input("Введите число типов с коробля: "))
crw = []

for _ in range(n):
    nme, sts = input("Имена утопленников и статус его: ").split()
    crw.append((nme, sts))

w_c = []
m = []
cpt = ""

for nme, sts in crw:
    if sts in ["woman", "child"]:
        w_c.append(nme)
    elif sts == "man":
        m.append(nme)
    elif sts == "captain":
        cpt = nme

evac_order = w_c + m + [cpt]

for member in evac_order:
    print(member)