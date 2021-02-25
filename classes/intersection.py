class Intersection:
    def __init__(self, position, streets):
        self.id = position
        self.streets = streets
        self.total_cars = self.get_total_cars_passing_through()
        self.streets_to_schedule, self.num_streets_to_schedule = self.get_num_incoming_streets_to_schedule()

    def get_num_incoming_streets_to_schedule(self):
        num = 0
        streets_to_schedule = []
        for street in self.streets:
            if street.driving_through() > 0:
                num += 1
                streets_to_schedule.append(street.name)

        return streets_to_schedule, num

    def get_total_cars_passing_through(self):
        total = 0
        for street in self.streets:
            total += self.get_total_cars_passing_through()

    def get_schedule(self):
        schedule = f'{self.id}\n'
        schedule += f'{self.num_streets_to_schedule}\n'
        for s in self.streets_to_schedule:
            schedule += f'{s.name} {s.driving_through()/self.total_cars}'
