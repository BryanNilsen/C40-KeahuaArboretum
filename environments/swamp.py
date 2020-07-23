from animals import Stagnant
from .environment import Environment


class Swamp(Environment):

    def __init__(self, name):
        Environment.__init__(self, name)
        self.animal_max = 8
        self.plant_max = 12
        self.current_speed = 0

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    def add_animal(self, animal):
        try:
            if animal.current_speed == 0:
                self.animals.append(animal)
            else:
                raise AttributeError()

        except AttributeError:
            print("Only animals that like stagnant water can be added to the swamp.")
            input("\n\nPress any key to continue...")

    def __str__(self):
        return f'{self.name}'
