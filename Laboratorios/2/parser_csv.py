import csv
import numpy as np


def load_words(file_name):
    parsed_list = []
    file_CSV = open(file_name)
    data_CSV = csv.reader(file_CSV)

    for row in data_CSV:
        for index in row:
            parsed_list.append(index)
    return parsed_list


def add_decorators(words, decorator, n):
    concatenate_string = decorator * n
    for index in range(len(words)):
        words[index] = concatenate_string + \
            words[index].lower() + concatenate_string
    return(words)

# Fix


def get_sequences(words, n):
    sequence_array = []
    temp_string = ""
    for index in range(len(words)):
        for constant in range(len(words[index])):
            temp_string = str(words[index])
            temp_string = temp_string[constant:constant+n]
            if temp_string not in sequence_array and len(temp_string) == n:
                sequence_array.append(temp_string)
                sequence_array.sort()
    return sequence_array
