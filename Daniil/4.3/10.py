def make_linear(lst: list):
    ans = []
    for i in lst:
        if isinstance(i, int):
            ans.append(i)
        else:
            ans.extend(make_linear(i))
    return ans
