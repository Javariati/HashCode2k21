import csv


def import_csv(filename, delimiter=','):
    data = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)

        for row in csv_reader:
            data.append(row)

    return data
