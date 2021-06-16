'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''


xyz = (i for i in range(5))
print(xyz)

for i in xyz:
    print(i)