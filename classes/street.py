class Street:
    def __init__(self, start, end, name, length):
        self.start = start
        self.end = end
        self.name = name
        self.length = length
        self.driving_through = 0

    def driving_through(self):
        return self.driving_through

    def add_car_driving_through(self):
        self.driving_through += 1

    def is_you(self, name):
        return name == self.name

    def __repr__(self):
        return self.name + " " + str(self.driving_through)
