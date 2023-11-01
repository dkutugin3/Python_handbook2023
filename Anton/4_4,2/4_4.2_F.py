def order(*args: str) -> str:
    global in_stock
    keys = ["coffee", "milk", "cream"]
    menu = {"Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
            "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
            "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
            "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
            "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
            "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1}
            }
    for arg in args:
        for key in keys:
            if menu[arg][key] > in_stock[key]:
                break
        else:
            for key in keys:
                in_stock[key] -= menu[arg][key]
            return arg

    return "К сожалению, не можем предложить Вам напиток"
