def solution():
    speed_petya = int(input())
    speed_vasya = int(input())
    speed_tolya = int(input())

    if speed_petya > speed_vasya and speed_petya > speed_tolya:
        print('Петя')
    elif speed_vasya > speed_tolya and speed_vasya > speed_petya:
        print('Вася')
    else:
        print('Толя')


def main():
    solution()


if __name__ == "__main__":
    main()
