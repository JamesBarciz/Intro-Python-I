#
def foo(x):  # 3
    x = 12  # 4

a = 8  #  1  - Immutable (8 is 8 is 8 is 8)

foo(a)  # 2

# print(a)
# Strings also immutable - must make a new string
def baz(x):
    print(x)
    x = x.upper()
    print(x)

s = 'hello'
baz(s)
