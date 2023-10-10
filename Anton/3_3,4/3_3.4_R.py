from itertools import product


def solution():
    st = input()
    print(f"a b c f")
    for (a, b, c) in product((0, 1), repeat=3):
        print(f"{a} {b} {c} {int(eval(st))}")


def main():
    solution()


if __name__ == "__main__":
    main()
