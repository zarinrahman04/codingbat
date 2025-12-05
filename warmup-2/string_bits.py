def string_bits(s):
    result = ""
    for i in range(0, len(s), 2):
        result += s[i]
    return result

print(string_bits('Hello'))       # Hlo
print(string_bits('Hi'))          # H
print(string_bits('Heeololeo'))   # Hello

