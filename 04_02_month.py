'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

user_input = input("What month? Enter 1-12:  ")

month = {'1':'January',
         '2':'February',
         '3':'March',
         '4':'April',
         '5':'May',
         '6':'June',
         '7':'July',
         '8':'August',
         '9':'September',
         '10':'October',
         '11':'November',
         '12':'December'}

if user_input in month:
    print(month[user_input])
else:
    print('Other.')


user_int = int(user_input)
if user_int in range(1,12):
    if user_int == 1:
        print('January.')
    elif user_int == 2:
        print('February')
    elif user_int == 3:
        print('March')
    elif user_int == 4:
        print('April')
    elif user_int == 5:
        print('May')
    elif user_int == 6:
        print('June')
    elif user_int == 7:
        print('July')
    elif user_int == 8:
        print('August')
    elif user_int == 9:
        print('September')
    elif user_int == 10:
        print('October')
    elif user_int == 11:
        print('November')
    elif user_int == 12:
        print('December')
else:
    print('Other.')
