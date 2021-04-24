'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

i = 4.5
print(i)

j = float(i)
print(j, type(j))

k = int(j)
print(k, type(k))

l = j // k
print(l)


first = int(input("Please enter a number. "))
sec = int(input("Enter another number. "))

product = first * sec

print("The product of the two numbers is {}.".format(product))
