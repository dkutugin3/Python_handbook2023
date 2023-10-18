all_toys = dict()
for i in range(int(input())):
    s = input()
    s = s.replace(",", "")
    toys = set(s.split()[1:])
    for j in toys:
        all_toys[j] = all_toys.get(j, 0)
        all_toys[j] += 1
ans = [i for i in all_toys if all_toys[i] == 1]
print(*sorted(ans), sep="\n")
