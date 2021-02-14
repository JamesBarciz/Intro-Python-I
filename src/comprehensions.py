"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at:
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [n for n in range(1, 6)]

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y2 = [n ** 3 for n in range(10)]

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y3 = [s.upper() for s in a]

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

# What do you need between the square brackets to make it work?


if __name__ == "__main__":
    x = input("Enter comma-separated numbers: ").split(',')
    y4 = [int(n) for n in x if int(n) % 2 == 0]

    print(y)
    print('------------------')
    print(y2)
    print('------------------')
    print(y3)
    print('------------------')
    print(y4)
    print('------------------')
