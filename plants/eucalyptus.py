from .plant import Plant


class RainbowEucalyptus(Plant):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", sunlight="shade",
                       seeds_produced=8, insecticide_resistance="low")

    def __str__(self):
        return f"{self.species} ({str(self.id)[:8]})"
