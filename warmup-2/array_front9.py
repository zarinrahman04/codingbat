def array_front9(nums):
    # Only check the first 4 elements (or fewer if list is shorter)
    end = min(4, len(nums))
    
    for i in range(end):
        if nums[i] == 9:
            return True
    return False

print(array_front9([1, 2, 9, 3, 4]))   # True
print(array_front9([1, 2, 3, 4, 9]))   # False
print(array_front9([1, 2, 3, 4, 5]))   # False
