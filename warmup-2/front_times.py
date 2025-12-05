def front_times(s, n):
    front = s[:3]
    return front * n

print(front_times('Chocolate', 2))  # ChoCho
print(front_times('Chocolate', 3))  # ChoChoCho
print(front_times('Abc', 3))        # AbcAbcAbc

