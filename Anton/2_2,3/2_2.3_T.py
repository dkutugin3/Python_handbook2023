def solution():
    pr_hash = 0
    for i in range(int(input())):
        block = int(input())
        cur_hash = block % 256
        if cur_hash >= 100:
            print(i)
            exit(0)
        rand = (block - cur_hash) // 256 % 256
        info = (block - cur_hash - rand) // (256 ** 2)
        if cur_hash != (37 * (info + rand + pr_hash)) % 256:
            print(i)
            exit(0)
        pr_hash = cur_hash
    print(-1)


def main():
    solution()


if __name__ == "__main__":
    main()
