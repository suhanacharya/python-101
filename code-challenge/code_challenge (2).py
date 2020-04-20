# ask a user to enter their first name and store it in a variable
# ask a user to enter their last name and store it in a variable
# print their full name
# Make sure you have a space between first and last name
# Make sure the first letter of first name and last name is uppercase
# Make sure the rest of the name is lowercase

first_name = input("Enter first name: ")
second_name = input("Enter Second name: ")

first_name = first_name.lower()
first_name = first_name.capitalize()

second_name = second_name.lower()
second_name = second_name.capitalize()

name = first_name + " " + second_name

print(name)

