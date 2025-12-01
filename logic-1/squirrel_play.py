def squirrel_play(temp, is_summer):
    """
    Squirrels play if temp is 60..90, or 60..100 in summer.
    """
    upper = 100 if is_summer else 90
    return 60 <= temp <= upper

print(squirrel_play(70, False))  # True
print(squirrel_play(95, False))  # False    