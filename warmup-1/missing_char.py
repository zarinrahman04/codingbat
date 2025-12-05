def missing_char(s, n):
    return s[:n] + s[n+1:]

print(missing_char('kitten', 1))  # 'ktten'
print(missing_char('kitten', 0))  # 'itten'
print(missing_char('kitten', 4))  # 'kittn'

