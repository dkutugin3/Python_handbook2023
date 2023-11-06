from itertools import count


def cycle(it: list):
    return (it[i % len(it)] for i in count(0, 1))
