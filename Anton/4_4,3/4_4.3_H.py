def fibonacci(n: int) -> int:
    a, b = 0, 1
    yield a

    for num in range(1, n):
        b, a = b + a, b
        yield a
