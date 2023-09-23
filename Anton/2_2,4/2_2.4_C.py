def solution():
    num_of_row = 1
    a = 1
    stop = int(input())
    while a <= stop:
        i = 1
        while i <= num_of_row:
            print(a, end=" ")
            i += 1
            a += 1
            if a > stop:
                break
        else:
            print('')
            num_of_row += 1


def main():
    solution()


if __name__ == "__main__":
    main()
