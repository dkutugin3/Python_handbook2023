def recursive_sum(*args):
    if args:
        return recursive_sum(*args[:-1]) + args[-1]
    return 0
