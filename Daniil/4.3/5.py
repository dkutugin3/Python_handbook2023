def result_accumulator(f):
    q = []

    def edited(*args, method="accumulate", **kwargs):
        nonlocal q
        q.append(f(*args, **kwargs))
        if method == "drop":
            buffer = q.copy()
            q.clear()
            return buffer

    return edited
