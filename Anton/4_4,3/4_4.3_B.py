def recursive_digit_sum(num: int) -> int:
    if num == 0:
        return 0
    return num % 10 + recursive_digit_sum(num // 10)
