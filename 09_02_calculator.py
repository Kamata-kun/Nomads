'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


try:
    num1 = int(input("Please enter the dividend: "))
    num2 = int(input("Please enter the divisor: "))
except ValueError:
    print("You must enter a valid integer.")
else:
    try:
        print(f"The quotient is {num1 / num2}.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
