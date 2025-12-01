def lucky_sum(a, b, c):
    """
    Return the sum of a, b, c.
    But if a value is 13, it and all values to its right count as 0.
    """
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

print(lucky_sum(1, 2, 3))   # 6
print(lucky_sum(1, 2, 13))  # 3