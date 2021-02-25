import sys

from utils.load_csv import import_csv
from classes.car import Car
##from classes.intersection import Intersection
from classes.street import Street
from classes.intersection import Intersection


def find_street(name, array):
    for street in array:
        if street.is_you(name):
            return street


def binary_search(arr, x):
    l = 0
    r = len(arr)

    while l <= r:
        m = l + ((r - l) // 2)

        if arr[m].name < x:
            r = m - 1
        elif arr[m].name > x:
            l = m + 1
        else:
            return arr[m]

    return -1


def calcola_tutto(path):
    first_line, streets, paths = import_csv(path)
    first_line_raw = first_line

    D = first_line_raw[0]
    I = first_line_raw[1]
    S = first_line_raw[2]
    V = first_line_raw[3]
    F = first_line_raw[4]

    total_streets = []
    total_cars = []
    intersections = []
    intersections_id = []

    for idx, street in enumerate(streets):
        total_streets.append(Street(street[0], street[1], street[2], street[3]))
        intersection_id = street[1]
        if intersections_id.count(intersection_id) > 0:
            for int in intersections:
                if int.id == intersection_id:
                    int.add_street(total_streets[idx])
                    break
        else:
            intersection = Intersection(intersection_id, [total_streets[idx]])
            intersections.append(intersection)
            intersections_id.append(intersection_id)

    for path in paths:
        total_cars.append(Car(path[0], path[1:]))

    sorted_streets = sorted(total_streets, reverse=True, key=Street.name)

    for car in total_cars:
        for street in car.streets:
            binary_search(sorted_streets, street).add_car_driving_through()

    for intersection in intersections:
        intersection.set_total_cars_passing_through()
        intersection.set_num_incoming_streets_to_schedule()

    # intersections = sorted(intersections, reverse=True, key=Intersection.total_cars)
    right_intersections = []

    for intersection in intersections:
        if intersection.total_cars > 0:
            right_intersections.append(intersection)


    print(len(right_intersections))

    for intersection in right_intersections:
        print(intersection)


def salva_soluzione(file_path):
    original_stdout = sys.stdout  # Save a reference to the original standard output

    with open('solutions/' + file_path, 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        calcola_tutto('inputs/' + file_path)
        sys.stdout = original_stdout  # Reset the standard output to its original value


if __name__ == "__main__":
    arr = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

    for file in arr:
        print("elaboro " + file + "\n")
        salva_soluzione(file)
