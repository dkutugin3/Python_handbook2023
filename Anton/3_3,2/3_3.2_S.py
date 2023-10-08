def solution():
    toys = {}
    ans = []
    for n in range(int(input())):
        inp = str(input()).split(': ')
        for toy in set(inp[1].split(', ')):
            toys[toy] = toys.get(toy, 0) + 1

    for item in toys.items():
        if item[1] == 1:
            ans.append(item[0])
    ans.sort()
    print(*ans, sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
