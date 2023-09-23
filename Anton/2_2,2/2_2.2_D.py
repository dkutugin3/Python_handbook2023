def solution():
    speeds = tuple(int(input()) for i in range(3))

    if speeds[0] > speeds[1]:
        if speeds[2] > speeds[0]:
            print("1. Толя", "2. Петя", "3. Вася", sep='\n')
        elif speeds[2] < speeds[1]:
            print("1. Петя", "2. Вася", "3. Толя", sep='\n')
        else:
            print("1. Петя", "2. Толя", "3. Вася", sep='\n')
    else:
        if speeds[2] > speeds[1]:
            print("1. Толя", "2. Вася", "3. Петя", sep='\n')
        elif speeds[2] < speeds[0]:
            print("1. Вася", "2. Петя", "3. Толя", sep='\n')
        else:
            print("1. Вася", "2. Толя", "3. Петя", sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
