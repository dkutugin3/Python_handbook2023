def prime_divs(x: int) -> set:
    div = 2
    divs = set()
    while x != 1:
        if x % div == 0:
            x //= div
            divs.add(div)
        else:
            div += 1
    return divs


def solution():
    nums = list(set(map(int, str(input()).split("; "))))
    ans = {}

    for idx, num in enumerate(nums):
        num_divs = prime_divs(num)
        for i in range(idx + 1, len(nums)):
            if not num_divs.intersection(prime_divs(nums[i])):
                ans[num] = ans.get(num, []) + [nums[i]]
                ans[nums[i]] = ans.get(nums[i], []) + [num]

    for item in sorted(ans.items()):
        if item[1]:
            print(item[0], end=" - ")
            print(*sorted(item[1]), sep=", ")


def main():
    solution()


if __name__ == "__main__":
    main()
