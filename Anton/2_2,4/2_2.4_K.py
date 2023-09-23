def is_prime(x):
    div = 2
    if x < 2:
        return False
    while div < int(x ** 0.5 + 1):
        if x % div == 0:
            return False
        else:
            div += 1
    return True


def solution():
    count = 0
    for i in range(int(input())):
        if is_prime(int(input())):
            count += 1
    print(count)


def main():
    solution()


if __name__ == "__main__":
    main()
