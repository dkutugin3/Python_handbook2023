class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0 or (d == 0 and a == 0):
        raise NoSolutionsError
    elif a == b == c == 0:
        raise InfiniteSolutionsError
    return ((-b - d**0.5) / (2 * a), (-b + d**0.5) / (2 * a))
