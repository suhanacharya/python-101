# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z

first_name = input("Enter First name: ")
if first_name[0] == "A" or first_name[0] == "B":
    print(first_name + " should be in room AB")
elif first_name[0] == "C" or first_name[0] == "D":
    print(first_name + " should be in room CD")
else:
    last_name = input("Enter Last name: ")
    if last_name[0] == "Z":
        print(first_name + last_name + " should be in room Z")
    else:
        print(first_name + " " + last_name + " should be in room OTHER")