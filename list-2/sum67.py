def sum67(nums):
    total = 0
    in_block = False   #are we inside a 6..7 block?

    for n in nums:
        if in_block:
            if n == 7:        #end of the block
                in_block = False
            continue          #skip everything until block ends

        if n == 6:            #start a new block
            in_block = True
            continue

        total += n            #normal number

    return total

print(sum67([1, 2, 2]))   # 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))   # 5
print(sum67([1, 1, 6, 7, 2]))   # 4

