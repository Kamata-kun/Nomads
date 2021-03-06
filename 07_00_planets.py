'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    '''Models a planet'''
    def __init__(self, name, color, system):
        self.name = name
        self.color = color
        self.system = system

    def __str__(self):
        return f"{self.name} is a {self.color} planet in the {self.system}."


earth = Planet('Earth','blue','solar system')
mars = Planet('Mars','red','solar system')

print(earth)
print(mars)

print(Planet('Venus','brown','solar system'))