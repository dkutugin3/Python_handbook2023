def solution():
    counter = 0
    for i in range(int(input())):
        if ((inp := str(input()))[:len(inp) // 2:]) == (inp[-1:-(len(inp) // 2) - 1: -1]):
            counter += 1
    print(counter)


def main():
    solution()


if __name__ == "__main__":
    main()
