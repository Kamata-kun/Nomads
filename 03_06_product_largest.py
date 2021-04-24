'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

listA = input("Please enter a list of ten numbers separated by spaces. (ie: 1 2 3 4) ")

my_List = listA.split(" ")

h = 0
for i in my_List:
    if int(i) > h:
        h = int(i)

print('The highest number is',h)

j = 1
for k in my_List:
    j = j * int(k)

print('The product of all of these numbers is',j)
