from itertools import cycle


def secret_replace(string: str, **rules) -> str:
    for (old, news) in rules.items():
        for new in cycle(news):
            if old not in string:
                break
            string = string.replace(old, new, 1)

    return string
