from itertools import islice, cycle

data = []
for i in range(int(input())):
    data.append(input())

count = int(input())
print(*list(islice(cycle(data), count)), sep="\n")
