'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''


string_1 = input("Please enter a string of words below! :")

new_list = string_1.split(" ")

new_dict = {}

for j in new_list:
    if j in new_dict:
        new_dict[j] += 1
    else:
        new_dict[j] = 1

print(max(new_dict.items(), key=lambda x: x[1]))

