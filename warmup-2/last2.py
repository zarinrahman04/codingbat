def last2(s):
    # If the string is too short, no possible matches
    if len(s) < 2:
        return 0
    
    last_two = s[-2:]   # the substring we are matching
    count = 0
    
    # Loop through all but the very last position 
    for i in range(len(s) - 2):
        if s[i:i+2] == last_two:
            count += 1
    return count

print(last2('hixxhi'))      # 1
print(last2('xaxxaxaxx'))   # 1
print(last2('axxxaaxx'))    # 2
