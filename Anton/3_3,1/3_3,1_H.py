def solution():
    ans = []
    for i in range(int(input())):
        row = str(input()).split(" ")
        if "зайка" not in row:
            ans.append("Заек нет =(")
        else:
            pos = 0
            for i in row:
                if i != "зайка":
                    pos += len(i) + 1
                else:
                    ans.append(pos + 1)
                    break
    print(*ans, sep='\n')


def main():
    solution()


if __name__ == "__main__":
    main()
