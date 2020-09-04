# Use UPER to tackle a problem

# def centered_avg(array):
'''Get the mean of two ints around center of array'''
# At least 3 integers
# Sort array
# Can be duplicates - if 3 center dups, ignore one
# Can be even number of ints - floor division
# Exclude largest and smallest values
# Mean of outer ints

# Sorting
def cent_avg(a):
    print(a)
    a.sort()
    print(a)
    middle = a[1:-1]
    print(middle)
    total = 0
    for v in middle:
        total += v
    
    return total // len(middle)

print(cent_avg([1, 1, 5, 5, 10, 8, 7]))
