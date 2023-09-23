def solution():
    answ = 0
    for i in range(int(input())):
        is_there_a_rabbit = 0
        while (inp := str(input())) != "ВСЁ":
            if inp == "зайка":
                is_there_a_rabbit = 1
        else:
            answ += is_there_a_rabbit
    print(answ)


def main():
    solution()


if __name__ == "__main__":
    main()
