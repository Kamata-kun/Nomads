'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''



dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

dict_3 = {}

for i in dict_1:
    if i not in dict_3:
        dict_3[i]=dict_1[i]

for j in dict_2:
    if j not in dict_3:
        dict_3[j]=dict_2[j]
    else:
        dict_3[j]=dict_3[j] + dict_2[j]

print(dict_1)
print(dict_2)
print("Result: ",dict_3)
