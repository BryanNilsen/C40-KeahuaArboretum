from animals import Aquatic


class Stagnant(Aquatic):

    def __init__(self):
        super().__init__()
        self.stagnant = True
