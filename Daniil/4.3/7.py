def same_type(f):
    def edited(*args):
        if len(args) == 0:
            return f(*args)
        for i in args:
            if not isinstance(i, type(args[0])):
                print("Обнаружены различные типы данных")
                return None
        return f(*args)

    return edited
