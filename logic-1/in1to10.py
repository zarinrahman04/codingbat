def in1to10(n, outside_mode):
    """
    Return True if n is in 1..10 inclusive,
    unless outside_mode is True, in which case
    return True if n <= 1 or n >= 10.
    """
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10

print(in1to10(5, False))  # True
print(in1to10(11, False))  # False
print(in1to10(11, True))  # True
