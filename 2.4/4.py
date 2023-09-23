n = int(input())
a = [_ for i in range(n) for _ in input()]
print(sum(map(int, a)))
