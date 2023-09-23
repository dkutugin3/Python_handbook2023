def solution():
    nums = tuple(int(input()) for i in range(3))
    if nums[0] % 10 == nums[1] % 10 and nums[0] % 10 == nums[2] % 10:
        print(nums[0] % 10)
    else:
        print(nums[0] // 10)


def main():
    solution()


if __name__ == "__main__":
    main()
