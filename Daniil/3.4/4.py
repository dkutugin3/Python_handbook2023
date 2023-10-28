from itertools import accumulate

data = input().replace(" ", " |").split()
for i in accumulate(data):
    print(i.replace("|", " "))
