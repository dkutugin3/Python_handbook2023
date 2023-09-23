def solution():
    for i in range(int(input())):
        for j in range(3 + i, -1, -1):
            if j == 0:
                print(f"Старт {i + 1}!!!")
            else:
                print(f"До старта {j} секунд(ы)")


def main():
    solution()


if __name__ == "__main__":
    main()
