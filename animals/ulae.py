from animals import Animal
from animals import Saltwater
from animals import Swimming


class Ulae(Animal, Saltwater, Swimming):

    def __init__(self):
        Animal.__init__(self, "Ulae")
        Saltwater.__init__(self)
        Swimming.__init__(self)
        self.__prey = {"Sea Anenonme", "Worms"}

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
