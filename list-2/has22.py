def has22(nums):
    """
    Return True if there is a 2 next to another 2.
    """
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

print(has22([1, 2, 2]))   #true
print(has22([1, 2, 1, 2]))   #false
print(has22([2, 1, 2]))   #false