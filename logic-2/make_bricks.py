def make_bricks(small, big, goal):
    """
    You have small (1 inch) and big (5 inch) bricks.
    Return True if you can reach exactly 'goal' inches.
    """
    # Maximum inches we can get from big bricks
    max_big_use = min(big, goal // 5)

    # After using big bricks, how many inches left?
    remaining = goal - max_big_use * 5

    # We can make the remaining length if we have enough small bricks
    return remaining <= small

print(make_bricks(3, 1, 8))   # true
print(make_bricks(3, 1, 9))   # false