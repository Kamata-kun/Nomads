'''
Using f-strings, print out the name, last name, and favorite
office supply item of each person in the given dictionary,
formatted like so:

LASTNAME, Name           Office supply item
LONGERLASTNAME, Name     Office supply item

'''

office = {
    1: {"full_name": "Michael Scott", "item": "world's best boss mug"},
    2: {"full_name": "Dwight Schrute", "item": "pepper spray"},
    3: {"full_name": "Jim Halpert", "item": "phone"},
    4: {"full_name": "Pam Beesly", "item": "post-its"},
    5: {"full_name": "Ryan Howard", "item": "business cards"},
    6: {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    7: {"full_name": "Kevin Malone", "item": "m&ms"},
    8: {"full_name": "Meredith Palmer", "item": "flask"},
    9: {"full_name": "Angela Martin", "item": "cat food"},
    10: {"full_name": "Oscar Martinez", "item": "calculator"},
    11: {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    12: {"full_name": "Kelly Kapoor", "item": "People magazine"},
    13: {"full_name": "Toby Flenderson", "item": "files"},
    14: {"full_name": "Creed Bratton", "item": "mung beans"},
    15: {"full_name": "Darryl Philbin", "item": "forklift"},
}

for i in office:
    office[i]["full_name"] = office[i]["full_name"].split(' ')

for j in office:
    if len(office[j]["full_name"][-1]) <= 5:
        print(f'{office[j]["full_name"][-1].upper():5s}, {office[j]["full_name"][0]:15s} {office[j]["item"]}')
    elif len(office[j]["full_name"][-1]) <= 6:
        print(f'{office[j]["full_name"][-1].upper():6s}, {office[j]["full_name"][0]:14s} {office[j]["item"]}')
    elif len(office[j]["full_name"][-1]) == 7:
        print(f'{office[j]["full_name"][-1].upper():7s}, {office[j]["full_name"][0]:13s} {office[j]["item"]}')
    elif len(office[j]["full_name"][-1]) == 8:
        print(f'{office[j]["full_name"][-1].upper():8s}, {office[j]["full_name"][0]:12s} {office[j]["item"]}')
    elif len(office[j]["full_name"][-1]) == 9:
        print(f'{office[j]["full_name"][-1].upper():9s}, {office[j]["full_name"][0]:11s} {office[j]["item"]}')
    elif len(office[j]["full_name"][-1]) == 10:
        print(f'{office[j]["full_name"][-1].upper():10s}, {office[j]["full_name"][0]:10s} {office[j]["item"]}')
