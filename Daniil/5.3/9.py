import re


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


def has_cyrillic(text):
    return bool(re.search("[\u0400-\u04ff]", text))


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    for char in name:
        if not has_cyrillic(char):
            raise CyrillicError

    if name.capitalize() != name:
        raise CapitalError
    return name


def string_validator(*args):
    for string in args:
        if not isinstance(string, str):
            raise TypeError


def user_validation(last_name, first_name, username, **kwargs):
    if kwargs or not last_name or not first_name or not username:
        raise KeyError
    string_validator(last_name, first_name, username)
    name_validation(last_name)
    name_validation(first_name)
    username_validation(username)
    return {"last_name": last_name, "first_name": first_name, "username": username}
