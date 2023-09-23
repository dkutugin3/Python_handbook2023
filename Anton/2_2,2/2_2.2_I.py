def solution():
    name = chr(ord("Я") + 1)
    for i in range(3):
        if (next_name := str(input())) < name:
            name = next_name
    print(name)


def main():
    solution()


if __name__ == "__main__":
    main()
