path = input()
tail_length = int(input())
with open(path, encoding="utf-8", mode="r") as file:
    data = [i for i in file]
    print(*data[-tail_length:], sep="")
