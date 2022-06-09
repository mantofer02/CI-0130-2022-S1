from time import time
from typing import Concatenate
import numpy as np
import random

DECORATOR = "$"


def calculate_transitions(words, sequences):
    prob_matrix = np.zeros(shape=(len(sequences), len(sequences)))
    prob_matrix.dtype = np.dtype(np.float64)

    n = len(sequences[0])

    for i in range(len(sequences)):
        counter = 0
        for element in words:
            index = element.find(sequences[i])
            if index != -1:
                for j in range(len(sequences)):
                    if (element[index + 1: index + 1 + n] == sequences[j]):
                        prob_matrix[i][j] += 1
                        counter += 1
        if counter != 0:
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

    final_state = False
    position = 0
    row = transition[0]

    while not final_state:

        random_value = r.random()
        for i in range(len(row)):
            if random_value < row[i]:
                position = i
                break
            else:
                random_value = random_value - row[i]

        if position == 0:
            final_state = True
        else:
            word += sequences[position][-1]
            row = transition[position]

    print(get_probability(model=model, word="mew"))
    return word.replace(DECORATOR, "").capitalize()


def get_probability(model, word):
    prob_matrix = model[0]
    sequences = model[1]

    word = word.lower()
    concatenate_string = DECORATOR * len(sequences[0])
    word = concatenate_string + word + concatenate_string

    probability = float(0)
    n = len(sequences[0])

    for i in range(len(sequences)):
        index = word.find(sequences[i])
        if index != -1:
            for j in range(len(sequences)):
                if (word[index + 1: index + 1 + n] == sequences[j]):
                    if probability == float(0):
                        probability += prob_matrix[i][j]
                    else:
                        probability = probability * prob_matrix[i][j]

    return probability
