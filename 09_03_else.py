'''
Write a script that demonstrates a try/except/else.

'''


try:
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a second number: "))
except ValueError:
    print("You must enter a valid integer.")
else:
    print(f"The product of the two numbers is {num1 * num2}.")
