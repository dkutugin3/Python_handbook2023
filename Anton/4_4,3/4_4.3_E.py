def result_accumulator(f):
    result_queue = []

    def dec(*args, method="accumulate"):
        nonlocal result_queue

        result_queue.append(f(*args))

        if method == "drop":
            buff = result_queue.copy()
            result_queue = []
            return buff

        else:
            return None

    return dec
