class Intersection:

    def __init__(self, position, streets=[]):
        self.id = position
        self.streets = streets
        self.total_cars = 0
        self.streets_to_schedule, self.num_streets_to_schedule = [], 0

    def total_cars(self):
        return self.total_cars

    def set_num_incoming_streets_to_schedule(self):
        num = 0
        streets_to_schedule = []
        for street in self.streets:
            if street.driving_through > 0:
                num += 1
                streets_to_schedule.append(street)

        self.streets_to_schedule = streets_to_schedule
        self.num_streets_to_schedule = num

    def set_total_cars_passing_through(self):
        total = 0
        for street in self.streets:
            total += street.driving_through

        self.total_cars = total

    def get_schedule(self):
        schedule = f'{self.id}\n'
        schedule += f'{self.num_streets_to_schedule}\n'
        for s in self.streets_to_schedule:
            schedule += f'{s.name} {s.driving_through / self.total_cars}\n'

        return schedule

    def add_street(self, street):
        self.streets.append(street)

    def __repr__(self):
        return self.get_schedule()
