def validate(a):
    if not isinstance(a, int):
        raise TypeError
    if (a <= 0) or ((a % 2) != 0):
        raise ValueError


def only_positive_even_sum(a, b):
    list(map(validate, [a, b]))
    return a + b
