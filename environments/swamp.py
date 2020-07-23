from .environment import Environment
# import sys
# sys.path.append('../')

# from environments import Stagnant


class Swamp(Environment):

    def __init__(self, name):
        Environment.__init__(self, name)
        self.animal_max = 8
        self.plant_max = 12
        # self.inhabitants = []

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    def add_animal(self, animal):
        # don't add more than capacity
        if len(self.animals) < self.animal_max:
            self.animals.append(animal)
        # throw error if you try

    # def addInhabitant(self, item):
        # if not isinstance(item, IStagnant):
        #     raise TypeError(f"{item} is not of type IStagnant")
        # self.inhabitants.append(item)

    def __str__(self):
        return f'{self.name}'
