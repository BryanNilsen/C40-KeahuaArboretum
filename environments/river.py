import os
from animals import Aquatic
from .environment import Environment


class River(Environment):

    def __init__(self, name):
        Environment.__init__(self, name, animal_max=12, plant_max=6)
        self.current_speed = 12

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
            else:
                raise AttributeError(
                    "Cannot add saltwater animals to a river")

        except AttributeError:
            print("Cannot add non-aquatic, or saltwater animals to a river")
            input("\n\nPress any key to continue...")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")

    def __str__(self):
        return f'{self.name}'
