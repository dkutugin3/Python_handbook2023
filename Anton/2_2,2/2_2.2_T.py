def solution():
    res = chr(ord('я') + 1)
    for i in range(3):
        if 'зайка' in (inp := str(input())).split(" "):
            res = min(res, inp)
    print(res, len(res))


def main():
    solution()


if __name__ == "__main__":
    main()
