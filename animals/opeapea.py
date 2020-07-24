from animals import Animal
from animals import Terrestrial
from animals import Flying
from animals import HighElevation
from .attributes import Trees


class Opeapea(Animal, Terrestrial, Flying, HighElevation, Trees):

    def __init__(self):
        Animal.__init__(self, "Ope'ape'a", release_age=5)
        Terrestrial.__init__(self)
        Flying.__init__(self)
        HighElevation.__init__(self)
        Trees.__init__(self)
        self.__prey = {"Leaves", "Mosquitoes", "Flies"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Ope'ape'a ate {prey} for a meal")
        else:
            print(f"The Ope'ape'a rejects the {prey}")

    def __str__(self):
        return f"Ope'ape'a ({str(self.id)[:8]})"
