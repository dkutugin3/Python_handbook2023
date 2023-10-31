def can_eat(knight: tuple, lunch: tuple) -> bool:
    if sorted([abs(knight[0] - lunch[0]), abs(knight[1] - lunch[1])]) == [1, 2]:
        return True
    return False
