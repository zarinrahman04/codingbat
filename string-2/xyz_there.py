def xyz_there(s):
    for i in range(len(s) - 2):
        if s[i:i+3] == "xyz":
            # If it's at the start or NOT preceded by "."
            if i == 0 or s[i-1] != '.':
                return True
    return False

print(xyz_there('abcxyz'))    # True
print(xyz_there('abc.xyz'))   # False
print(xyz_there('xyz.abc'))   # True

