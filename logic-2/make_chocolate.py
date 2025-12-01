def make_chocolate(small, big, goal):
    """
    Use big bars (5kg) first, then small bars (1kg).
    Return the number of small bars needed.
    Return -1 if it cannot be done exactly.
    """
    # Maximum number of big bars we can use without exceeding goal
    max_big_use = min(big, goal // 5)

    # Remaining weight after using big bars
    remaining = goal - max_big_use * 5

    # Check if we have enough small bars to cover the rest
    if remaining <= small:
        return remaining
    else:
        return -1

print(make_chocolate(4, 1, 9))   # 4
print(make_chocolate(4, 1, 10))  # -1