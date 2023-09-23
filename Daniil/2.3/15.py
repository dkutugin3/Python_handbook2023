n = int(input())
a = [1 if 'зайка' in input() else 0 for i in range(n)]
print(sum(a))
