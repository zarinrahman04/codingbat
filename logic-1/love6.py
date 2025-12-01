def love6(a, b):
    """
    Return True if either number is 6,
    or if their sum or absolute difference is 6.
    """
    return (
        a == 6 or
        b == 6 or
        a + b == 6 or
        abs(a - b) == 6
    )

print(love6(6, 4))   # true
print(love6(4, 5))   # false