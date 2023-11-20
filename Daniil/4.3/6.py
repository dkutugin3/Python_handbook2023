def merge(a: list, b: list):
    result = []
    while a and b:
        if a[0] > b[0]:
            result.append(b.pop(0))
        else:
            result.append(a.pop(0))
    return result + a + b


def merge_sort(lst):
    if len(lst) > 1:
        return merge(merge_sort(lst[:len(lst) // 2]), merge_sort(lst[len(lst) // 2:]))
    return lst
