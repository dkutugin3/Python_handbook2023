def make_linear(some_list: list):
    ans = []
    for el in some_list:
        if isinstance(el, list):
            [ans.append(i) for i in make_linear(el)]
        else:
            ans.append(el)
    return ans
