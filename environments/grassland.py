from .environment import Environment


class Grassland(Environment):

    def __init__(self, name):
        Environment.__init__(self, name, animal_max=22, plant_max=15)

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    def add_animal(self, animal):
        try:
            if animal.likes_grass:
                self.animals.append(animal)
            else:
                raise AttributeError()

        except AttributeError:
            print("Only animals that like grass can be added to the grassland.")
            input("\n\nPress any key to continue...")

    def add_plant(self, plant):
        try:
            # if plant.freshwater and plant.requires_current:
            self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")

    def __str__(self):
        return f'{self.name}'
