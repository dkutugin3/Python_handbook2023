def can_eat(horse: tuple, x: tuple) -> bool:
    x1, y1 = horse
    x2, y2 = x
    if {abs(x1 - x2), abs(y1 - y2)} == {1, 2}:
        return True
    return False
