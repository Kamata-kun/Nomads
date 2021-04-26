'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''


user_str = input("Please enter a string. ")

str_list = user_str.split()

print(str_list)

tuple_A=[]

for i in str_list:
    tuple_A.append(tuple(i))

print(tuple_A)
