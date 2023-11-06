def answer(f):
    def dec(*args, **kwargs):
        return f"Результат функции: {f(*args, **kwargs)}"

    return dec
