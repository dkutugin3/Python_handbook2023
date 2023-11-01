def recursive_sum(*nums: int) -> int:
    if len(nums) == 0:
        return 0
    return nums[-1] + recursive_sum(*nums[:-1:])
