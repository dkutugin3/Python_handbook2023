def solution():
    name = str(input())
    price = int(input())
    weight = int(input())
    note = int(input())

    check = f"Чек"
    change = f"{note - price * weight}руб"
    all = f"{price * weight}руб"
    note = f"{note}руб"
    price = f"{weight}кг * {price}руб/кг"

    print(f"{check:=^35}",
          f"Товар:{name: >29}",
          f"Цена:{price: >30}",
          f"Итого:{all: >29}",
          f"Внесено:{note: >27}",
          f"Сдача:{change: >29}",
          35 * "=",
          sep="\n")


def main():
    solution()


if __name__ == "__main__":
    main()
