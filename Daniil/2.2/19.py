def rasst_00(x, y):
    return (x ** 2 + y ** 2) ** 0.5


def parabola(x, y):
    res = 0.25 * (x - 5) * (x + 7)
    if y >= res:
        return True
    else:
        return False


def pryamaya(x, y):
    res = 5 * x / 3 + 35 / 3
    if y <= 5 and y <= res:
        return True
    return False


def circle(x, y):
    if rasst_00(x, y) <= 5:
        return True
    return False


def check(x, y):
    if x >= 0 and y >= 0:
        return circle(x, y)
    if x <= 0 <= y:
        return pryamaya(x, y)
    return parabola(x, y)


def main():
    x = float(input())
    y = float(input())
    if rasst_00(x, y) > 10:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
        exit()
    if check(x, y):
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")


if __name__ == "__main__":
    main()
