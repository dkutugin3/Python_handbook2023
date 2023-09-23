def solution():
    print("Как Вас зовут?")
    reply = str(input())
    print(f"Здравствуйте, {reply}!")
    print("Как дела?")
    if (reply := str(input())) == "хорошо":
        print("Я за вас рада!")
    elif reply == "плохо":
        print("Всё наладится!")


def main():
    solution()


if __name__ == "__main__":
    main()
