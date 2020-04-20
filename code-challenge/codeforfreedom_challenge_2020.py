no_of_animals = int(input())
indicies = []
animals = []

animals_dictionary = {}

# Taking inputs as two different lists
for i in range(no_of_animals):
	indicies.append(int(input()))  # Positions into indices list
for i in range(no_of_animals):
	animals.append(input())  # Animals into animals list

# Creating a dictionary with two lists as position : "animal" pairs
animals_dictionary = {indicies[i]:animals[i] for i in range(no_of_animals)}

#print(animals_dictionary)

# Creating a counter to check if current posision = desired position 
counter = 1

# Iterating through the dictionary
for index, animal in animals_dictionary.items():
	# We need to modify to upper or lowecase only if 
	# current position is not desired position
	if index != counter:  
		if index == len(animal):
			# Since animal has same length as
			# the value of desired position, make it uppercase
			animals_dictionary[index] = animal.upper()  
		else:
			animals_dictionary[index] = animal.lower()

	counter = counter + 1  # Increment counter every iteration

# Sort the dictionary with respect to keys(positions)
animals_dictionary = dict(sorted(animals_dictionary.items()))


# Output formatting: 
print()

for index, animal in animals_dictionary.items():
	print(animal)

print()
