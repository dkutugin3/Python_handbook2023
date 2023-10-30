def gcd(x: int, y: int) -> int:
    while x != 0:
        x, y = y % x, x
    return y
