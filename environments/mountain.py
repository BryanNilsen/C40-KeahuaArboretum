from .environment import Environment


class Mountain(Environment):

    def __init__(self, name):
        Environment.__init__(self, name)
        self.animal_max = 6
        self.plant_max = 4

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    def add_animal(self, animal):
        # check for appropriate properties and throw errors
        self.animals.append(animal)

    def __str__(self):
        return f'{self.name}'
