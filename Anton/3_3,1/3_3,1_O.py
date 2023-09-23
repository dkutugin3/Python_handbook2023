from math import gcd


def solution():
    print(gcd(*tuple(map(int, str(input()).split(" ")))))  # я уже писал этот НОД,
    # можно не надо, за нас это уже сделали другие люди


def main():
    solution()


if __name__ == "__main__":
    main()
