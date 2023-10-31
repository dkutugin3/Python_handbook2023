from itertools import chain


def merge(a: tuple, b: tuple) -> tuple:
    a = list(a)
    b = list(b)
    ans = []

    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            ans.append(a[0])
            del a[0]
        else:
            ans.append(b[0])
            del b[0]
    return tuple(chain(ans, a, b))
