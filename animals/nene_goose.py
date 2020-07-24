from animals import Animal
from animals import Terrestrial
from animals import Flying
from .attributes import Grass


class NeneGoose(Animal, Terrestrial, Flying, Grass):

    def __init__(self):
        Animal.__init__(self, "Nene Goose", release_age=7)
        Terrestrial.__init__(self)
        Flying.__init__(self)
        Grass.__init__(self)
        self.__prey = {"Grass"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The nene goose ate {prey} for a meal")
        else:
            print(f"The nene goose rejects the {prey}")

    def __str__(self):
        return f"Nene Goose ({str(self.id)[:8]})"
