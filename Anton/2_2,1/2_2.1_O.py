def solution():
    hours = int(input())
    minutes = int(input())
    time = int(input())

    hours = (hours + (minutes + time) // 60) % 24
    minutes = (minutes + time) % 60

    hours = str(hours)
    minutes = str(minutes)

    print(f"{hours:0>2}:{minutes:0>2}")


def main():
    solution()


if __name__ == "__main__":
    main()
