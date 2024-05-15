def type_controller(*args):
    for a in args:
        item_type = type(a[0])
        for i in range(len(a)):
            if not isinstance(a[i], item_type):
                raise TypeError


def sort_controller(*args):
    for a in args:
        for i in range(len(a) - 1):
            if a[i] >= a[i + 1]:
                raise ValueError


def merge(x1, x2):
    if not (hasattr(x1, "__iter__") and hasattr(x2, "__iter__")):
        raise StopIteration
    type_controller(x1, x2)
    if not isinstance(x1[0], type(x2[0])):
        # говно
        raise TypeError
    sort_controller(x1, x2)
    ans = []
    buff = [*x1, *x2]
    while buff:
        ans.append(min(buff))
        buff.remove(min(buff))
    return tuple(ans)
