from .contains_plants import ContainsPlants
from .contains_animals import ContainsAnimals
from animals import Identifiable


class Environment(Identifiable, ContainsPlants, ContainsAnimals):

    def __init__(self, name):
        Identifiable.__init__(self)
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        self.name = name

    def __str__(self):
        return self.name
