def merge(x1: tuple, x2: tuple) -> tuple:
    ans = []
    buff = [*x1, *x2]
    while buff:
        ans.append(min(buff))
        buff.remove(min(buff))
    return tuple(ans)
