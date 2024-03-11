n = int(input())
ans = []
for _ in range(n):
    a, b, s = input().split("&")
    ans.append(s[int(a)::2][:int(b)])
print(*ans, sep="\n")
