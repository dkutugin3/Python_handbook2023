def add(x: dict, name: str, *args: str):
    for key in args:
        if not x.get(key):
            x[key] = []
        x[key].append(name)


def solution():
    ans = {}
    for i in range(int(input())):
        add(ans, *str(input()).split(' '))
    print(*sorted(ans.get(str(input()), ["Таких нет"])), sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
