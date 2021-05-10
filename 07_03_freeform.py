'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''


class Baseball:
    def __init__(self, name, city, mascot):
        self.name = name
        self.city = city
        self.mascot = mascot

    def __str__(self):
        return f"The mascot of the {self.city} {self.name} is {self.mascot}."

cubs = Baseball('Cubs', 'Chicago', 'Clark')
phillies = Baseball('Phillies','Philadelphia','the Phillie Phanatic')
nationals = Baseball('Nationals','Washingiton','Screech')

print(cubs)
print(phillies)
print(nationals)

cubs.mascot = 'none'

print(cubs)



class Snake:
    def __init__(self,name,venom,color):
        self.name = name
        self.venom = venom
        self.color = color

    def __str__(self):
        if self.venom == 'yes'.lower():
            return f'The {self.name} is a(n) {self.color} venomous snake.'
        else:
            return f'The {self.name} is a(n) {self.color} non-venomous snake.'

cobra = Snake('King Cobra','yes','green')
garter = Snake('Garter Snake','yes','olive')
python = Snake('Albino Python','no','white')

print(cobra)
print(garter)
print(python)

garter.venom = 'no'

print(garter)


class Day:
    def __init__(self, appointments, visits, calls):
        self.appointments = appointments
        self.visits = visits
        self.calls = calls

    def __add__(self, other):
        total_appointments = self.appointments + other.appointments
        total_visits = self.visits + other.visits
        total_calls = self.calls + other.calls
        return Day(total_appointments, total_visits, total_calls)

    def __str__(self):
        return f'There were {self.appointments} appointments, ' \
               f'{self.visits} visits and {self.calls} calls.'


day1 = Day(6,4,2)
day2 = Day(8,3,4)

print(day1)
print(day2)

day3 = day1 + day2

print(day3)