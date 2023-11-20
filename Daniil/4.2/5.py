def to_string(*a, sep=" ", end="\n"):
    a = [str(i) for i in a]
    return sep.join(a) + end
