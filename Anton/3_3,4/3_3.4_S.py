from itertools import product


def solution():
    st = input()

    keys = set()
    for lt in st:
        if lt.isupper():
            keys.add(lt)
    keys = sorted(list(keys))

    print(*keys, 'F', sep=' ')
    for values in product((0, 1), repeat=len(keys)):
        variables = {key: value for (key, value) in zip(keys, values)}
        print(*values, sep=' ', end=' ')
        print(int(eval(st, variables)), end='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
