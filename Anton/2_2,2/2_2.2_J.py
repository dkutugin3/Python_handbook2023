def solution():
    num = int(input())
    pass1 = (num % 10) + (num // 10) % 10
    pass2 = (num // 10) % 10 + (num // 100)
    if pass1 > pass2:
        print(pass1, pass2, sep="")
    else:
        print(pass2, pass1, sep="")


def main():
    solution()


if __name__ == "__main__":
    main()
