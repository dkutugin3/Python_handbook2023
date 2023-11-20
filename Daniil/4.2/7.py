results = {0: [], 1: []}


def enter_results(*args):
    global results
    for i, k in enumerate(args):
        results[i % 2].append(k)


def get_sum():
    return round(sum(results[0]), 2), round(sum(results[1]), 2)


def get_average():
    return (round(sum(results[0]) / len(results[0]), 2),
            round(sum(results[1]) / len(results[1]), 2))
