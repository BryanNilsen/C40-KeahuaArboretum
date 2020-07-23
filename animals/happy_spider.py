from animals import Animal
from animals import Terrestrial
from animals import Walking
from animals import Stagnant


class HawaiianHappyFaceSpider(Animal, Terrestrial, Walking, Stagnant):

    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-Face Spider")
        Terrestrial.__init__(self)
        Walking.__init__(self)
        Stagnant.__init__(self)
        self.__prey = {"Crickets", "Flies"}
        self.leg_count = 8

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The Hawaiian Happy-Face Spider ate {prey} for a meal")
        else:
            print(f"The Hawaiian Happy-Face Spider rejects the {prey}")

    def __str__(self):
        return f"Hawaiian Happy-Face Spider ({str(self.id)[:8]})"
