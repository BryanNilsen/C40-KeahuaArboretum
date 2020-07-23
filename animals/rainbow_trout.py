from animals import Animal
from animals import Freshwater
from animals import Swimming


class RainbowTrout(Animal, Freshwater, Swimming):

    def __init__(self):
        Animal.__init__(self, "Rainbow Trout")
        Freshwater.__init__(self)
        Swimming.__init__(self)
        self.__prey = {"Crickets", "Worms", "Flies"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Rainbow Trout ate {prey} for a meal')
        else:
            print(f'The Rainbow Trout rejects the {prey}')

    def __str__(self):
        return f'Rainbow Trout ({str(self.id)[:8]})'
