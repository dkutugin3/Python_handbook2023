from sys import stdin

ans = 0
for i in stdin:
    ans += sum(map(int, i.split()))
print(ans)
