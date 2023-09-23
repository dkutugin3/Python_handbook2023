def solution():
    name = str(input())
    number = int(input())
    print(f"Группа №{number // 100}.",
          f"{number % 10}. {name}.",
          f"Шкафчик: {number}.",
          f"Кроватка: {(number // 10) % 10}.",
          sep="\n")


def main():
    solution()


if __name__ == "__main__":
    main()
