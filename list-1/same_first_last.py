def same_first_last(nums):
    """
    Return True if the list has length 1 or more AND 
    the first and last elements are the same.
    """
    return len(nums) >= 1 and nums[0] == nums[-1]

print(same_first_last([1, 2, 3]))      # False
print(same_first_last([1, 2, 3, 1]))   # True
print(same_first_last([1, 2, 1]))      # True