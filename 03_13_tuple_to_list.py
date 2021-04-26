'''
Write a script that takes a tuple and turns it into a list.

'''

tuple_A = ([1, 2], [3, 5], [4, 7], [12, 18])

list_A = []

for i in tuple_A:
    for j in i:
        list_A.append(j)


print("Given tuple ",tuple_A)
print("The list is ",list_A)
