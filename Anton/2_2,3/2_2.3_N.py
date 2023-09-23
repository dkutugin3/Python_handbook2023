def is_prime(x):
    if x <= 1:
        return "NO"
    for div in range(2, int(x ** 0.5 + 1)):
        if x % div == 0:
            return "NO"
    else:
        return "YES"


def solution():
    print(is_prime(int(input())))


def main():
    solution()


if __name__ == "__main__":
    main()
