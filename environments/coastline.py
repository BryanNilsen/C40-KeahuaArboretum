from .environment import Environment
from animals import Aquatic


class Coastline(Environment):

    def __init__(self, name):
        Environment.__init__(self, name, animal_max=15, plant_max=3)

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    # add animal method to check for properties and throw errors
    def add_animal(self, animal):
        try:
            if animal.aquatic and (animal.cell_type == "hypotonic" or animal.cell_type == "isotonic"):
                self.animals.append(animal)
            else:
                raise AttributeError(
                    "Cannot add freswater animals to a coastline")

        except AttributeError:
            print("Cannot add non-aquatic, or freshwater animals to a coastline")
            input("\n\nPress enter to continue...")

    def __str__(self):
        return f'{self.name}'
