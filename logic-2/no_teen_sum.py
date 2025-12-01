def fix_teen(n):
    """
    Teens 13–19 become 0, except for 15 and 16.
    """
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n


def no_teen_sum(a, b, c):
    """
    Return the sum of a, b, c, treating 'teen' values as 0.
    Uses fix_teen() to avoid repeating logic.
    """
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 2, 3))    # 6
print(no_teen_sum(2, 13, 1))   # 3  