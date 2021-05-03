'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

# This wasn't a dictionary, it was a list? So I made a dictionary.

nested_quotes = {}
nested_quotes[1] = {}
nested_quotes[1]['Name'] = {'First':'Isaac','Middle':'','Last':'Asimov'}
nested_quotes[1]['Quote'] = '"I do not fear computers. I fear lack of them."'
nested_quotes[2] = {}
nested_quotes[2]['Name'] = {"First":"Emo","Middle":"","Last": "Philips"}
nested_quotes[2]['Quote'] = '"A computer once beat me at chess, but it was no match for me at kick boxing."'
nested_quotes[3] = {}
nested_quotes[3]['Name'] = {"First":"Edsger","Middle":"W.","Last": "Dijkstra"}
nested_quotes[3]['Quote'] = '"Computer Science is no more about computers than astronomy is about telescopes."'
nested_quotes[4] = {}
nested_quotes[4]['Name'] = {"First":"Bill","Middle":"","Last": "Gates"}
nested_quotes[4]['Quote'] ='"The computer was born to solve problems that did not exist before."'
nested_quotes[5] = {}
nested_quotes[5]['Name'] = {"First":"Nathan","Middle":"","Last": "Myhrvold"}
nested_quotes[5]['Quote'] ='"Software is like entropy: It is difficult to grasp, weighs nothing, ' \
                             'and obeys the Second Law of Thermodynamics; i.e., it always increases."'
nested_quotes[6] = {}
nested_quotes[6]['Name'] = {"First_name":"Alan","Middle_init":"","Last_name": "Bennett"}
nested_quotes[6]['Quote'] = '"Standards are always out of date. That’s what makes them standards."'



for item in nested_quotes:
    print(f"{nested_quotes[item]['Quote']} - {nested_quotes[item]['Name']['Last']}, "
          f"{nested_quotes[item]['Name']['First']} {nested_quotes[item]['Name']['Middle']}")