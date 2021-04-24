'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''


inv_amt = float(input("What is the initial investment amount? "))
int_rate = float(input("What is the interest rate percentage? "))
inv_time = float(input("How many years will this money be invested? "))

# inv_amt + ((int_rate / 100) + 100) * inv_time

perc = ((int_rate/100)+100)

fut_val = inv_amt + (int_rate * inv_time)

print("After {} years, your ${} will have matured into ${}, assuming an interest rate of {}%.".format(int(inv_time), inv_amt, fut_val, int_rate))
