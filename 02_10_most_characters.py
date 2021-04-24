'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''


string1 = input("Please enter the first string. ")
string2 = input("Please enter a second string. ")
string3 = input("Please enter the third string. ")

print(len(string1)," ", string1)
print(len(string2)," ", string2)
print(len(string3)," ", string3)


if len(string1) > len(string2) and len(string1) > len(string3):
    print(len(string1), " ", string1)
elif len(string2) > len(string1) and len(string2) > len(string3):
    print(len(string2), " ", string2)
else:
    print(len(string3), " ", string3)
