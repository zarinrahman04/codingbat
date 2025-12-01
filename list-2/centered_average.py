def centered_average(nums):
    """
    Return the centered average: mean of the list after removing
    one smallest and one largest value. Use integer division.
    """
    nums_sorted = sorted(nums)
    trimmed = nums_sorted[1:-1]      # remove one min and one max
    return sum(trimmed) // len(trimmed)

print(centered_average([1, 2, 3, 4, 100]))   # 3
print(centered_average([1, 1, 5, 5, 10, 8, 7]))   # 5
print(centered_average([-10, -4, -2, -4, -2, 0]))   # -3