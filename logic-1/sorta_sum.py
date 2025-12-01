def sorta_sum(a, b):
    """
    Return a+b, except if the sum is between 10 and 19 inclusive,
    return 20 instead.
    """
    total = a + b
    if 10 <= total <= 19:
        return 20
    return total

print(sorta_sum(3, 4))   # 7
print(sorta_sum(9, 4))   # 20   