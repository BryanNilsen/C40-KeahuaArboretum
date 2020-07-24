from .environment import Environment


class Forest(Environment):

    def __init__(self, name):
        Environment.__init__(self, name, animal_max=20, plant_max=32)

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it"

    def add_animal(self, animal):
        try:
            if animal.likes_trees:
                self.animals.append(animal)
            else:
                raise AttributeError(
                    "Cannot add animals that don't like trees to a forest.")

        except AttributeError:
            print("Cannot add animals that don't like trees to a forest")
            input("\n\nPress any key to continue...")

    def __str__(self):
        return f'{self.name}'
