from utils.load_csv import import_csv
from classes.car import Car
##from classes.intersection import Intersection
from classes.street import Street


def find_street(name, array):
    for street in array:
        if street.is_you(name):
            return street


if __name__ == "__main__":
    first_line, streets, paths = import_csv('inputs/b.txt')
    first_line_raw = first_line

    D = first_line_raw[0]
    I = first_line_raw[1]
    S = first_line_raw[2]
    V = first_line_raw[3]
    F = first_line_raw[4]

    total_streets = []
    total_paths = []

    for street in streets:
        total_streets.append(Street(street[0], street[1], street[2], street[3]))

    for path in paths:
        for val in path[1:]:
            find_street(val, total_streets).add_car_driving_through()

    sorted_streets = sorted(total_streets, reverse=True, key=Street.driving_through)

    print(sorted_streets)
