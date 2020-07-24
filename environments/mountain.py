from .environment import Environment
from animals import HighElevation


class Mountain(Environment):

    def __init__(self, name):
        Environment.__init__(self, name, animal_max=6, plant_max=4)

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    def add_animal(self, animal):
        try:
            if animal.max_elevation > 2999:
                self.animals.append(animal)
            else:
                raise AttributeError()

        except AttributeError:
            print(
                "Animals that can't survive at high altitudes cannot be added to a mountain.")
            input("\n\nPress any key to continue...")

    def __str__(self):
        return f'{self.name}'
