from animals import Identifiable


class Animal(Identifiable):

    def __init__(self, species, release_age=0):
        Identifiable.__init__(self)
        self.species = species
        self.age = 0
        self.release_age = release_age

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"
