import csv


def load_words(file_name):
    parsed_list = []
    file_CSV = open(file_name)
    data_CSV = csv.reader(file_CSV)

    for row in data_CSV:
        for index in row:
            parsed_list.append(index)
    return parsed_list
