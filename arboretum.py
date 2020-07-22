class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rivers = []
        self.mountains = []
        self.grasslands = []
        self.forests = []
        self.swamps = []
        self.coastlines = []

        @property
        def rivers(self):
            return self.__rivers

        def annex_river(self, river):
            # duck type check here??
            self.__rivers.append(river)
