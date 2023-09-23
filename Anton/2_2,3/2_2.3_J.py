def solution():
    counter = {}
    while (key := str(input())) != "СТОП":
        val = int(input())
        counter[key] = counter.get(key, 0) + val
    print(counter.get("СЕВЕР", 0) - counter.get("ЮГ", 0), counter.get("ВОСТОК", 0) - counter.get("ЗАПАД", 0), sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
