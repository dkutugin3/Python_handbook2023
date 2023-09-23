a = list(map(int, list(input())))
ans = [sum(a[1:]), sum(a[:2])]
ans.sort(reverse=True)
print(*ans, sep="")
