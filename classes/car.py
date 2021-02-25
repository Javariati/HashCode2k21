class Car:
    def __init__(self, number_of_streets, streets):
        self.numberOfStreets = number_of_streets,
        self.streets = streets

    def getNumberOfStreets(self):
        return self.numberOfStreets

    def getStreets(self):
        return self.streets

    def __repr__(self):
        return str(self.streets)
