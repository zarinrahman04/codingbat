def near_ten(num):
    """
    Return True if num is within 2 of a multiple of 10.
    """
    r = num % 10
    return r <= 2 or r >= 8

print(near_ten(12))  # True
print(near_ten(17))  # False