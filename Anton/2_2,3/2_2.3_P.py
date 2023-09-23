def solution():
    inp = str(input())
    for i in range(len(inp) // 2):
        if inp[i] != inp[-(i + 1)]:
            print("NO")
            break
    else:
        print("YES")


def main():
    solution()


if __name__ == "__main__":
    main()
