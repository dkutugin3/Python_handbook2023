from sys import stdin

avg = []
for i in stdin:
    x1, x2 = i.split()[1:]
    avg.append(int(x2) - int(x1))
print(round(sum(avg) / len(avg)))
