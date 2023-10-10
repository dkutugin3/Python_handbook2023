def solution():
    print(*[f"{kid1} - {kid2}" for (kid1, kid2) in zip(str(input()).split(", "), str(input()).split(", "))], sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
