def order(*prefer):
    global in_stock
    menu = {"Эспрессо": {"coffee": 1, "milk": 0, "cream": 0},
            "Капучино": {"coffee": 1, "milk": 3, "cream": 0},
            "Макиато": {"coffee": 2, "milk": 1, "cream": 0},
            "Кофе по-венски": {"coffee": 1, "milk": 0, "cream": 2},
            "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
            "Кон Панна": {"coffee": 1, "milk": 0, "cream": 1}
            }
    keys = ("coffee", "cream", "milk")
    for cup in prefer:
        if may_cook(menu[cup]):
            return cup
    return "К сожалению, не можем предложить Вам напиток"


def may_cook(cup: dict):
    global in_stock
    if all([cup[i] <= in_stock[i] for i in cup.keys()]):
        in_stock = {i: (in_stock[i] - cup[i]) for i in cup.keys()}
        return True
    return False
