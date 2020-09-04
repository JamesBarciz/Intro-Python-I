a = [1, 2, 3, 4]

b = a

assert b == a

b[2] = 99  # Modifies same point in memory

print(a)  # a[2] ALSO = 99
