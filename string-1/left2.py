def left2(s):
    return s[2:] + s[:2]

print(left2('Hello'))  # 'lloHe'
print(left2('java'))   # 'vaja'
print(left2('Hi'))     # 'Hi'