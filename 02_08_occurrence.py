'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

str1 = input("Please enter a string. ")
lttr1 = input("Please specify a letter from that string. ")


i = 0
while i < len(str1):
    if str1[i] == lttr1:
        print("Result: ",i)
        break
    i += 1
