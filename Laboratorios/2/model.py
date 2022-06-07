
from operator import pos
import numpy as np
import random

# It is ready


def calculate_transitions(words, sequences):
    prob_matrix = np.zeros(shape=(len(sequences), len(sequences)))
    prob_matrix.dtype = np.dtype(np.float64)

    for i in range(len(sequences)):
        counter = 0
        for j in range(len(sequences)):
            occurency = sequences[i] + sequences[j]
            for element in words:
                times = element.count(occurency)
                prob_matrix[i][j] += times
                counter += times

        if (counter != 0):
            prob_matrix[i][:] = prob_matrix[i][:] / counter
    return prob_matrix


def add_decorators(words, decorator, n):
    concatenate_string = decorator * n
    for index in range(len(words)):
        words[index] = concatenate_string + \
            words[index].lower() + concatenate_string
    return(words)


def create_model(words, ngrams):
    decorator = '$'

    words_with_decorators = add_decorators(
        words, decorator=decorator, n=ngrams)

    sequences = get_sequences(words=words_with_decorators, n=ngrams)
    transition = calculate_transitions(
        words=words_with_decorators, sequences=sequences)

    return transition, sequences


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


def generate_word(model, seed):

    r = random.Random()
    r.seed(seed)
    transition = model[0]
    sequences = model[1]

    word = ''

    finalState = False
    position = 0
    row = transition[0]

    while not finalState:

        random_value = r.random()
        for i in range(len(row)):
            if random_value < row[i]:
                position = i
                break
            else:
                random_value = random_value - row[i]

        if position == 0:
            finalState = True
        else:
            word += sequences[position]
            row = transition[position]

    return word


def get_probability(model, word):
    pass
