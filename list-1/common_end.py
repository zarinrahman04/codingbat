def common_end(a, b):
    """
    Return True if the two lists have the same first element
    or the same last element.
    """
    return a[0] == b[0] or a[-1] == b[-1]

print(common_end([1, 2, 3], [7, 3]))   # True
print(common_end([1, 2, 3], [7, 3, 2]))   # False
print(common_end([1, 2, 3], [1, 3]))   # True