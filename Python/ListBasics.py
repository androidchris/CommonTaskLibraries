# Create a list of numbers:
numbers = [1,2,3,4,5]

# Other way to create a list:
 # list2 = list()

# Display the list of numbers:
print(numbers)

# Add the numbers in the list and display:
print(numbers[0] + numbers[1])

# Loop through the list:
for i in numbers:
    print(i)

# Create a List of Beatles members:
beatles = ['John', 'Paul', 'George', 'Ringo']

# Display beatles list to start:
print("Beatles to start: " + str(beatles))

# Determine number of items in a list:
# Convert to string and pass to len function.
print("Number of Beatles " + str(len(beatles)))

# Display all beatles except the first one:
print("Beatles members except first: " + str(beatles[1:]))

# Display the first two beatles:
print("The first two beatles: " + str(beatles[0:2]))

# Display the last two beatles:
print("Last two beatles: " + str(beatles[2:4]))

# Sort a list without changing the list:
print("Beatles temp sorted: " + str(sorted(beatles)))

# Display Beatles List before sort:
print("Beatles before perm sort: " + str(beatles))

# Sort the beatles permanently 
beatles.sort();

# Permanently sort a list:
print("Beatles after perm sorted: " + str(beatles))

# Reverse the order of beatles:
beatles.reverse()
print("Beatles permanently reversed: " + str(beatles))

# Adding a name to end of the list:
beatles.append('Pete')
print("Beatles w/ Pete added: " + str(beatles))

# Remove last element of list w/ pop:
beatles.pop();
print("Beatles after popping off Pete: " + str(beatles))

# Find the index value of a specific beatle:
indx = beatles.index('George')
print("The index of George is at: " + str(indx))

# Delete a beatle at specific index, in this case George:
del beatles[indx]
print("George deleted: " + str(beatles))