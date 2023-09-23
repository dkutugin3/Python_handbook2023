def solution():
    hours = int(input())
    minutes = int(input())
    time = int(input())

    hours = (hours + (minutes + time) // 60) % 24
    minutes = (minutes + time) % 60

    hours = "0" + str(hours)
    minutes = "0" + str(minutes)

    print(f"{hours[-2::]}:{minutes[-2::]}")


def main():
    solution()


if __name__ == "__main__":
    main()
