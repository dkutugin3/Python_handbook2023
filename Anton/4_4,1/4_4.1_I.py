def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    for div in range(2, int(x ** 0.5 + 1)):
        if x % div == 0:
            return False
    return True
      