def close_far(a, b, c):
    """
    One of b or c must be 'close' to a (diff <= 1),
    and the other must be 'far' from BOTH a and the close one (diff >= 2).
    """

    close_b = abs(a - b) <= 1
    close_c = abs(a - c) <= 1

    far_b = abs(a - b) >= 2 and abs(b - c) >= 2
    far_c = abs(a - c) >= 2 and abs(b - c) >= 2

    return (close_b and far_c) or (close_c and far_b)

print(close_far(1, 2, 10))  # true
print(close_far(1, 2, 3))   # false 