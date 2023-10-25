from timeit import timeit

print(round(timeit("s = '; '.join(str(x) for x in range(10 ** 7))", number=10), 3))
print(round(timeit("s = '; '.join([str(x) for x in list(range(10 ** 7))])", number=10), 3))