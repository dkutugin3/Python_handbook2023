def solution():
    nums = []
    for i in range(int(input())):
        nums.append(int(input()))
    power = int(input())
    print(*tuple(map(lambda x: x ** power, nums)), sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
