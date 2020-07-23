from .environment import Environment


class Grassland(Environment):

    def __init__(self, name):
        Environment.__init__(self, name, animal_max=22, plant_max=15)
        # self.inhabitants = []

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    # add animal method to check for properties and throw errors

    def __str__(self):
        return f'{self.name}'
