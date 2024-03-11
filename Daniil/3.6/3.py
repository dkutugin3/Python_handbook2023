numbers = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1]
a = [i for i in sorted(numbers, key=lambda x: x % 2)]
print(a)
