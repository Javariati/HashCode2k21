import csv


def import_csv(filename, delimiter=' '):
    data = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)

        count_row = 0
        street_number = 0
        streets = []
        paths = []
        first_line = None

        for row in csv_reader:
            if count_row == 0:
                print("Jack bravo")
                first_line = row
                street_number = int(row[2])
            elif count_row <= street_number:
                streets.append(row)
            else:
                paths.append(row)

            count_row += 1

    return first_line, streets, paths
