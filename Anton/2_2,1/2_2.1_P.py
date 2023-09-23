def solution():
    start_pos = int(input())
    finish_pos = int(input())
    speed = int(input())

    print(f"{(abs(finish_pos - start_pos) / speed):.2f}")


def main():
    solution()


if __name__ == "__main__":
    main()
