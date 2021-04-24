'''

Write a script that removes all duplicates from a list.

'''

list_A= [1, 2, 3, 4, 3, 4, 5]


list_B=[]

for i in list_A:
    if i not in list_B:
        list_B.append(i)

print(list_A)
print(list_B)
