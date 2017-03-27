# Create a Dictionary w/ Key/Value pairs:
numbers = {'Bob':'322', 'Mary':'110', 'Joe':'222'}

# Loop through the dictionary:
for i in numbers:
    print(i)

# Display the value associated w/ first element 'Bob':
print(numbers['Bob'])

# Create Beatles members w/ their instruments:
beatles = {'John':'Guitar', 'Paul':'Bass', 'George':'Guitar', 'Ringo':'Drums'}

# Display our beatles dictionary:
print("Beatles members: " + str(beatles))

# Display the instrument John plays:
print("John plays the " + str(beatles['John']))

# Display how many items are in the Dictionary:
print("There are " + str(len(beatles)) + " items in the Dictionary.")

# List the keys in a Dictionary:
print("The keys in the Dictionary: " + str(list(beatles.keys())))

# List the values in a Dictionary:
print("The values in the Dictionary: " + str(list(beatles.values())))

# Loop through Dictionary displaying name and instrument the person plays:
for name in beatles.keys():
    print(name + ' plays the ' + beatles[name])

# Using the get function to get a specific value
# out of a Dictionary.
print('Paul plays the ' + str(beatles.get('Paul')))

# Change the instruments that Paul plays:
beatles['Paul'] = ['Bass', 'Guitar', 'Keyboard']
print('Paul now plays all these: ' + str(beatles.get('Paul')))

# Add Pete to the Dictionary:
beatles['Pete'] = 'Drums'
print("New Beatles member Dictionary: " + str(beatles))

# Pop Pete off the Dictionary:
beatles.pop('Pete')
print("Pop Pop Pop goes the Pete : " + str(beatles))
