def solution():
    num = 500
    step = 500
    print(num)
    while (inp := str(input())) != "Угадал!":
        step = round(step / 2 + 0.1)
        if step == 0:
            step = 1
        if inp == "Больше":
            num += step
        else:
            num -= step
        print(num)


def main():
    solution()


if __name__ == "__main__":
    main()
