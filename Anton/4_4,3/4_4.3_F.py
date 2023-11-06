from itertools import chain


def merge(a: list, b: list) -> list:
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
    return list(chain(ans, a, b))


def merge_sort(some_list: list) -> list:
    if len(some_list) < 2:
        return some_list
    first_half = some_list[:len(some_list) // 2:]
    second_half = some_list[len(some_list) // 2::]
    return merge(merge_sort(first_half), merge_sort(second_half))
