import re


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
