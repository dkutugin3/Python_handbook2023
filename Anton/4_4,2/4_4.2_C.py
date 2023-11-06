def gcd(*nums: int) -> int:
    nums = list(nums)

    while len(nums) > 1:
        nums[0], nums[1] = nums[1] % nums[0], nums[0]
        if nums[0] == 0:
            del nums[0]

    return nums[-1]
