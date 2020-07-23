from .environment import Environment
from animals import Aquatic


class Forest(Environment):

    def __init__(self, name):
        Environment.__init__(self, name, animal_max=20, plant_max=32)

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    def add_animal(self, animal):
        # check for appropriate properties and throw errors
        self.animals.append(animal)

    def __str__(self):
        return f'{self.name}'
