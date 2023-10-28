from itertools import count

a, b, c = map(float, input().split())
for i in count(a, c):
    if i <= b:
        print(f"{i:.2f}")
    else:
        break
