def solution():
    length = int(input())
    text = []
    for n in range(int(input())):
        text.append(str(input()))
        if length > len(text[-1]) + 3:
            length -= len(text[-1])
        elif length > 3:
            text[-1] = text[-1][:length - 3] + "..."
            length = 0
        elif length == 0:
            text.pop(-1)
    print(*text, sep="\n")


def main():
    solution()


if __name__ == "__main__":
    main()
