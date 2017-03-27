# Loop Examples:
number = 1

# While Loop:
while number < 11:
    print(number)
    number += 1

balance = 1000
rate = 1.02
years = 0

# Another While Loop example:
while balance < 5000:
    balance *= rate
    years += 1

print("It takes " + str(years) + " years to reach $5000.")

# For Loop using a range:
for i in range(1,11):
    print(i)

# More For Loop examples:
sum = 0

numbers = range(1, 11)

for i in numbers:
    sum += i

print(sum)

