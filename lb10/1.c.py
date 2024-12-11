with open(r'/Users/m1/Downloads/lab10/file4.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()


p = []
for line in lines:
    parts = line.strip().split()
    name = ' '.join(parts[:-1])
    score = int(parts[-1])
    p.append((name, score))


max_score = max(p[1] for p in p)


prize_score = max(p[1] for p in p if p[1] < max_score)


for name, score in p:
    if score == prize_score:
        print(f"Призер: {name}, баллы: {score}")
        break
