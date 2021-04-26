'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''


user_string = input("Please enter a string of characters!\n: ")

new_dict = {}

for i in user_string:
    if i not in new_dict:
        new_dict[i] = 1
    else:
        new_dict[i] += 1

print("Result= ",new_dict)
