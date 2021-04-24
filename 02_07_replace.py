'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

str_input = input("Please enter a string of characters. ")
symb_input = input("Please enter a special character. ")

first = str_input[0]
print(first)
new_str =""
for i in str_input:
    if i == first:
        i = symb_input
    new_str += i

print(new_str)
