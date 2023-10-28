g1 = input().replace(",", "").split()
g2 = input().replace(",", "").split()
ans = zip(g1, g2)
for i, j in ans:
    print(f"{i} - {j}")
