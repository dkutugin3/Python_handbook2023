def solution():
    man = set()
    ovs = set()
    N = range(int(input()))
    M = range(int(input()))
    for n in N:
        man.add(str(input()))
    for m in M:
        ovs.add(str(input()))
    ans = man.intersection(ovs)
    if not ans:
        print("Таких нет")
    else:
        print(len(ans))


def main():
    solution()


if __name__ == "__main__":
    main()
