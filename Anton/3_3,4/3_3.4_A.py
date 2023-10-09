def solution():
    print(*[f"{idx}. {obj}" for (idx, obj) in enumerate(str(input()).split(' '), 1)], sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
