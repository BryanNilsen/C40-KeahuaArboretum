from animals import Animal
from animals import Freshwater
from animals import Swimming
from animals import Stagnant


class Kikakapu(Animal, Freshwater, Swimming, Stagnant):

    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        Freshwater.__init__(self)
        Swimming.__init__(self)
        Stagnant.__init__(self)
        self.__prey = {"Crickets", "Worms", "Mosquitos"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The kīkākapu ate {prey} for a meal')
        else:
            print(f'The kīkākapu rejects the {prey}')

    def __str__(self):
        return f'Kīkākapu ({str(self.id)[:8]})'
