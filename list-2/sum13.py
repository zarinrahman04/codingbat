def sum13(nums):
    total = 0
    skip_next = False

    for n in nums:
        if skip_next:      #skip the number after 13
            skip_next = False
            continue

        if n == 13:        #skip 13 and mark next number to skip
            skip_next = True
            continue

        total += n

    return total

print(sum13([1, 2, 2, 1]))   # 6
print(sum13([1, 1]))   # 2
print(sum13([1, 2, 2, 1, 13]))   # 6

