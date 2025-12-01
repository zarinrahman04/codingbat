def date_fashion(you, date):
    """
    Return 0=no, 1=maybe, 2=yes based on stylishness.
    """
    # If either person has very low style → no
    if you <= 2 or date <= 2:
        return 0
    
    # If either person has very high style → yes
    if you >= 8 or date >= 8:
        return 2
    
    # Otherwise → maybe
    return 1

print(date_fashion(5, 5))   # 1
print(date_fashion(5, 10))  # 2
print(date_fashion(5, 2))   # 0