def cycle(lst: list):
    i = 0
    while True:
        yield lst[i % len(lst)]
        i += 1
