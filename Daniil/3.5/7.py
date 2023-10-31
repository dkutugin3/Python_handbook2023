path = input()
with open(path, encoding="utf-8", mode="r") as file:
    data = []
    for i in file:
        data.extend(map(int, i.rstrip("\n").split()))
    print(len(data))
    print(len([k for k in data if k > 0]))
    print(min(data))
    print(max(data))
    print(sum(data))
    print(f"{sum(data) / len(data):.2f}")
