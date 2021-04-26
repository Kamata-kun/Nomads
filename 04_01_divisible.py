'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''


user_num = 0

while user_num < 1 or user_num > 1000000000:
    user_num = int(input("Please enter a number between 1 and 1,000,000,000.  "))
    if user_num % 3 == 0:
        print("This number is divisible by 3!")
    else:
        print("This number is not divisible by 3.")
