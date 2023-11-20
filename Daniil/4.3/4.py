def answer(f):
    def edited(*args, **kwargs):
        return "Результат функции: " + str(f(*args, **kwargs))
    return edited

