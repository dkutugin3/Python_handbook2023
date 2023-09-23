def solution():
    counter = 0
    for i in range(int(input())):
        counter += str(input()).split(" ").count("зайка")
    print(counter)


def main():
    solution()


if __name__ == "__main__":
    main()
