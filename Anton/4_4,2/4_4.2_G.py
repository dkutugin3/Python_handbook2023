def enter_results(*results: int) -> None:
    global a1, a2
    try:
        a1
    except NameError:
        a1 = []
    try:
        a2
    except NameError:
        a2 = []

    for (idx, result) in enumerate(results, 1):
        if idx % 2 > 0:
            a1.append(result)
        else:
            a2.append(result)


def get_sum() -> (float, float):
    return round(sum(a1), 2), round(sum(a2), 2)


def get_average() -> (float, float):
    return round(sum(a1) / len(a1), 2), round(sum(a2) / len(a2), 2)
