class Car:
    def __init__(self, starting_point, number_of_streets, streets):
        self.startingPoint = starting_point,
        self.numberOfStreets = number_of_streets,
        self.streets = streets

    def getStartingPoint(self):
        return self.startingPoint

    def getNumberOfStreets(self):
        return self.numberOfStreets

    def getStreets(self):
        return self.streets
