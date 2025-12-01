def caught_speeding(speed, is_birthday):
    """
    Return 0=no ticket, 1=small ticket, 2=big ticket.
    Speed limits are 5 higher on your birthday.
    """
    # Birthday gives a 5-mph grace
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2

print(caught_speeding(60, False))  # 0
print(caught_speeding(65, False))  # 1  