from animals import Animal
from animals import Flying
from animals import Terrestrial
from .attributes import Trees


class Pueo(Animal, Terrestrial, Flying, Trees):

    def __init__(self):
        Animal.__init__(self, "Ulae")
        Terrestrial.__init__(self)
        Flying.__init__(self)
        Trees.__init__(self)
        self.__prey = {"Rats", "Mice"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The 'ulae ate {prey} for a meal")
        else:
            print(f"The 'ulae rejects the {prey}")

    def __str__(self):
        return f"Pueo ({str(self.id)[:8]})"
