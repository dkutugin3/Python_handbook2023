a = input()
b = input()
res = [int(i) for i in a + b]
res.sort()
print(str(res[-1]) + str(sum(res[1:-1]) % 10) + str(res[0]))
