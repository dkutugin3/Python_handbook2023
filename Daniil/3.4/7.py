from itertools import combinations

data = []
for i in range(int(input())):
    data.append(input())
for i, j in combinations(data, r=2):
    print(f"{i} - {j}")
