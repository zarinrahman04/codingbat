def round_sum(a, b, c):
    """
    Return the sum of a, b, c after rounding each using round10().
    """
    return round10(a) + round10(b) + round10(c)


def round10(num):
    """
    Round num to nearest multiple of 10:
    - If rightmost digit < 5 → round down
    - If rightmost digit >= 5 → round up
    """
    remainder = num % 10
    if remainder < 5:
        return num - remainder
    else:
        return num + (10 - remainder)

print(round_sum(16, 17, 18))  # 50
print(round_sum(12, 13, 14))  # 40