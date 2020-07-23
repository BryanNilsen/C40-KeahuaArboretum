from .contains_plants import ContainsPlants
from .contains_animals import ContainsAnimals
from animals import Identifiable


class Environment(Identifiable, ContainsPlants, ContainsAnimals):

    def __init__(self, name, animal_max=0, plant_max=0):
        Identifiable.__init__(self)
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        self.animal_max = animal_max
        self.plant_max = plant_max
        self.name = name

    def __str__(self):
        return self.name
