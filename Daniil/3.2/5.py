n = int(input())
m = int(input())
ans = set()
for i in range(n + m):
    ans = ans ^ {input()}

if len(ans) != 0:
    print(len(ans))
else:
    print("Таких нет")
