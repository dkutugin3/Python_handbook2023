def solution():
    name = str(input())
    price = int(input())
    weight = int(input())
    note = int(input())
    print("Чек",
          f"{name} - {weight}кг - {price}руб/кг",
          f"Итого: {int(price * weight)}руб",
          f"Внесено: {note}руб",
          f"Сдача: {note - int(price * weight)}руб",
          sep="\n")


def main():
    solution()


if __name__ == "__main__":
    main()
