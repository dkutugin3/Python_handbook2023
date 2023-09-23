a = map(int, input().split())
degree = int(input())
a = [i ** degree for i in a]
print(*a)
