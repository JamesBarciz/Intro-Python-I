#
def bar(x):
    x[2] = 99  # Updates the 3rd item

a = [1, 2, 3, 4]  # Mutable

bar(a)
print(a)
