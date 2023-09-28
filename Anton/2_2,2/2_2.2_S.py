def solution():
    x = float(input())
    y = float(input())
    if x ** 2 + y ** 2 <= 10 ** 2:
        if (y >= 0.25 * x ** 2 + 0.5 * x - 8.75) and (y <= 5 / 3 * x + 35 / 3) and (y <= 5) and (
                (x ** 2 + y ** 2 <= 5 ** 2) or x < 0 or y < 0):
            print("Опасность! Покиньте зону как можно скорее!")
        else:
            print("Зона безопасна. Продолжайте работу.")
    else:
        print("Вы вышли в море и рискуете быть съеденным акулой!")


def main():
    solution()


if __name__ == "__main__":
    main()
