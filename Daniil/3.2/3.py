n = int(input())
ans = set()
for i in range(n):
    ans = ans | set(input().split())
print(*ans, sep="\n")
