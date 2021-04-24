'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

my_String = input("Please enter a string of characters. ")

l = 0
while l < len(my_String):
    if my_String[l] in vowels:
        vowels[(my_String[l])] += 1
    l += 1

print(vowels)
