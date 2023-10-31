def is_palindrome(x):
    if isinstance(x, int):
        return str(x) == str(x)[::-1]
    if isinstance(x, str):
        return x == x[::-1]
    x = list(x)
    return x == x[::-1]
