class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def char_validation(s: str):
    for char in s:
        if (
            char
            not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
        ):
            raise BadCharacterError


def digit_start_validation(s: str):
    if s[0].isdigit():
        raise StartsWithDigitError


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    char_validation(username)
    digit_start_validation(username)
    return username
