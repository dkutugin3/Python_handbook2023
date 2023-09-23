n = int(input())
ans = ""
for _ in range(n):
    ans += str(max(map(int, list(input()))))
print(ans)
