def recursive_digit_sum(x):
    if x:
        return x % 10 + recursive_digit_sum(x // 10)
    return 0
