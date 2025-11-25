def has23(nums):
    """
    Return True if the list (length 2) contains a 2 or a 3.
    """
    return 2 in nums or 3 in nums

print(has23([2, 5]))   # True
print(has23([4, 3]))   # True
print(has23([4, 5]))   # False