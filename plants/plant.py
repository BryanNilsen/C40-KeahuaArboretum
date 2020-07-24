from animals import Identifiable


class Plant(Identifiable):

    def __init__(self, species, sunlight="full", seeds_produced=0, insecticide_resistance="low"):
        Identifiable.__init__(self)
        self.species = species
        self.sunlight = sunlight
        self.seeds_produced = seeds_produced
        self.insecticide_resistance = insecticide_resistance
