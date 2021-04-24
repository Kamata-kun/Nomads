'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

str_inp = input("Please enter a string of ten numbers, separated by commas. \n ie: 1,2,3 ")

list_A = str_inp.split(",")


print(list_A[1],list_A[3],list_A[5],list_A[7],list_A[9])
print(list_A[8],list_A[6],list_A[4],list_A[2],list_A[0])
