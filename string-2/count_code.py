def count_code(s):
    count = 0
    for i in range(len(s) - 3):
        if s[i:i+2] == "co" and s[i+3] == "e":
            count += 1
    return count

print(count_code('aaacodebbb'))     # Expected 1
print(count_code('codexxcode'))     # Expected 2
print(count_code('cozexxcope'))     # Expected 2
