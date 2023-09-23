def solution():
    menu = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
    for i in range(int(input())):
        print(menu[i % 5])


def main():
    solution()


if __name__ == "__main__":
    main()
