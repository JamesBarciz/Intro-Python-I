# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    if n % 2 == 0:
        return True

# Read a number from the keyboard
# num = input("Enter a number: ")
# num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


if __name__ == "__main__":
    # Locals
    num = input("Enter a number: ")
    num = int(num)

    if is_even(num) == True:
        print('Even!')
    else:
        print('Odd')