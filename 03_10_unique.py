'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

list_A = [1, 2, 6, 55, 2, 1, 'hi', 4, 12, 4, 13, 87]
list_B = []
for i in list_A:
    if i not in list_B:
        list_B.append(i)

print(list_A)
print(list_B)
