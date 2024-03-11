import itertools

n = int(input())
lst = []
ans = []
for _ in range(n):
    lst.append(list(map(int, input().replace(",", "").split())))
for a in itertools.product(*lst):
    ans.append(int("".join(map(str, a))))
print(*sorted(set(ans)), sep="\n")
