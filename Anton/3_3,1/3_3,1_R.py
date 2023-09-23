def solution():
    ans = []
    inp = str(input())
    prev = inp[0]
    counter = 0
    for i in inp + '*':
        if i != prev:
            ans.append((prev, counter))
            prev = i
            counter = 1
        else:
            counter += 1
    for el in ans:
        print(*el, sep=' ')


def main():
    solution()


if __name__ == "__main__":
    main()
