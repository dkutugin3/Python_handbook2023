def solution():
    ans = []
    for num in (str(input()).split(' ')):
        binnum = bin(int(num))[2::]
        stat = {"digits": len(binnum),
                "units": binnum.count('1'),
                "zeros": binnum.count('0')}
        ans.append(stat)
    print(ans)


def main():
    solution()


if __name__ == "__main__":
    main()
