from hashlib import sha256

poss = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def char_validation(s: str, pattern: str):
    for char in s:
        if char not in pattern:
            raise PossibleCharError


def string_validator(*args):
    for string in args:
        if not isinstance(string, str):
            raise TypeError


def password_validation(
    password, min_length=8, possible_chars=poss, at_least_one=str.isdigit
):
    string_validator(password, possible_chars)
    if len(password) < min_length:
        raise MinLengthError

    char_validation(password, possible_chars)
    if not any(map(at_least_one, list(password))):
        raise NeedCharError
    return sha256(password.encode()).hexdigest()
