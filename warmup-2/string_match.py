def string_match(a, b):
    count = 0
    # Only loop while both have characters left for a 2-char substring
    min_len = min(len(a), len(b))
    
    for i in range(min_len - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count

print(string_match('xxcaazz', 'xxbaaz'))   # 3
print(string_match('abc', 'abc'))          # 2
print(string_match('abc', 'axc'))          # 0
