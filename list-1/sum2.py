def sum2(nums):
    """
    Return the sum of the first two elements.
    If the list has fewer than 2 elements, sum what exists.
    """
    if len(nums) >= 2:
        return nums[0] + nums[1]
    elif len(nums) == 1:
        return nums[0]
    else:
        return 0

print(sum2([1, 2, 3]))   # 3
print(sum2([1, 1]))   # 2
print(sum2([1, 1, 1, 1]))   # 2
print(sum2([]))   # 0
print(sum2([9]))   # 9