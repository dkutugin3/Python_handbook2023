def same_type(f):
    def dec(*args, **kwargs):
        for arg in args:
            if not type(arg) is type(args[0]):
                print("Обнаружены различные типы данных")
                return None
        return f(*args, **kwargs)

    return dec
