from .environment import Environment


class Grassland(Environment):

    def __init__(self, name):
        Environment.__init__(self, name)
        self.inhabitants = []

    def animal_count(self):
        return f"This place has {len(self.inhabitants)} animals in it"

    def addInhabitant(self, item):
        # if not isinstance(item, IStagnant):
        #     raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)

    def __str__(self):
        return f'{self.name}'
