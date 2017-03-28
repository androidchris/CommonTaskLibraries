# Store a string:
myStr = 'string'

# Store a number:
number = 20

# Display full String:
print(myStr)

# Print the first letter of a String using array:
print(myStr[0])

# Print everything except the first char of the String:
print(myStr[1:])

# String concat example w/ converting number to a String:
print("It takes " + str(number) + " years to reach...")

# Create Variables:
a = 12
b = 3
age = 40

# Divide and display as whole number, no decimal:
print(a // b)

# Divide and display w/ decimal place:
print(a / b)

# Printing Hello 5 times:
print("Hello" * 5)

# Boolean tells if a string is inside anther string:
# true
print("day" in "today")

# false
print("no" in "today")

# Using String placeholders:(Old way of doing it, Python 2)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

# Displaying certain number of decimal places:
# 50 decimal places.
print("Pi is approximately %1.50f" % (22/7))

# Replacement field Syntax(Python 3 way)
# Allocate two spaces {0:2}
print("I am {0:2} years old.".format(age))

# Pi example using replacement fields.(Python 3 way)
# Allocate 1 for the 3 and 50 decimal places.
print("Pi is approximately {0:1.50f}".format(22/7))

# Replacement fields:(Python 3 way)
# Benefit is you can reuse the replacement field in multiple places
# You can't do this w/ the old python 2 way.
# Notice we have four months and 3 replacements, we use month 2 twice.
print("January: {2}, February: {0}, March: {2}, June: {1}".format(28, 30, 31))

