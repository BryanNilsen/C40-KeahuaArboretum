from .environment import Environment


class Coastline(Environment):

    def __init__(self, name):
        Environment.__init__(self, name)
        self.animal_max = 15
        self.plant_max = 3
        self.current_speed = 18

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    # add animal method to check for properties and throw errors
    def add_animal(self, animal):
        # don't add more than capacity
        if len(self.animals) < self.animal_max:
            self.animals.append(animal)
        # throw error if you try

    def __str__(self):
        return f'{self.name}'
