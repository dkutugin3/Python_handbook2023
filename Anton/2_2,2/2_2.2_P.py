def solution():
    speeds = tuple(int(input()) for i in range(3))

    if speeds[0] > speeds[1]:
        if speeds[2] > speeds[0]:
            first, second, third = 'Толя', '  Петя', 'Вася  '
        elif speeds[2] < speeds[1]:
            first, second, third = 'Петя', '  Вася', 'Толя  '
        else:
            first, second, third = 'Петя', '  Толя', 'Вася  '
    else:
        if speeds[2] > speeds[1]:
            first, second, third = 'Толя', '  Вася', 'Петя  '
        elif speeds[2] < speeds[0]:
            first, second, third = 'Вася', '  Петя', 'Толя  '
        else:
            first, second, third = 'Вася', '  Толя', 'Петя  '

    print(f"{first: ^24}", f"{second: <24}", f"{third: >24}", f"{'II': ^8}{'I': ^8}{'III': ^8}", sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
