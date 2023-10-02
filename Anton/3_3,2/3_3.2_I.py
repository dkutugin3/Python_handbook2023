def add(x: dict, *args: str):
    for key in args:
        x[key] = x.get(key, 0) + 1


def solution():
    counter = {}
    while (inp := str(input())) != '':
        add(counter, *inp.split(' '))
    for item in counter.items():
        print(*item, sep=' ')


def main():
    solution()


if __name__ == "__main__":
    main()
