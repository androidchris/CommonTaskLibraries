# Create variables:
number = 12
denom = 0

# Prevent dividing by zero:
if denom != 0:
    print(number/denom)
else:
    print('Division by zero is not allowed')

# Grade if/elif example:
grade = 72

# Letter graded based on number grade:
if grade >= 90:
    letterGrade = 'A'
elif grade >= 80:
    letterGrade = 'B'
elif grade >= 70:
    letterGrade = 'C'
elif grade >= 60:
    letterGrade = 'D'
else:
    letterGrade = 'F'

# Display the letter grade:
print(letterGrade)

