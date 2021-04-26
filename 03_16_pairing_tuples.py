'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

user_nums = input("Please enter a list of numbers, separated by a comma.\n(ie:1,2,3): ")

list_A = user_nums.split(',')

list_B = []

for i in list_A:
    list_B.append(int(i))

list_B.sort()

if len(list_B) % 2 != 0:
    list_B.append(0)

list_C = []
tuple_A = ()

it = iter(list_B)
for j in it:
    tuple_A = (j, next(it))
    list_C.append(tuple_A)

print(list_C)
