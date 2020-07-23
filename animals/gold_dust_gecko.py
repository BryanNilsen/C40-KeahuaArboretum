from animals import Animal
from animals import Terrestrial
from animals import Walking


class GoldDustDayGecko(Animal, Terrestrial, Walking):

    def __init__(self):
        Animal.__init__(self, "Ulae")
        Terrestrial.__init__(self)
        Walking.__init__(self)
        self.__prey = {"Crickets", "Flies"}
        self.leg_count = 4

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f"The gold dust day gecko ate {prey} for a meal")
        else:
            print(f"The gold dust day gecko rejects the {prey}")

    def __str__(self):
        return f"Gold Dust Day Gecko ({str(self.id)[:8]})"