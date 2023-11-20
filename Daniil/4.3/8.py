def fibonacci(a):
    x1 = 0
    x2 = 1
    while a > 0:
        yield x1
        x1, x2 = x2, x2 + x1
        a -= 1
