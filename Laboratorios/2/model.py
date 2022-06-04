
import numpy as np


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
        prob_matrix[i][:] = prob_matrix[i][:] / counter
    return prob_matrix


def create_model(words, ngrams):
    pass


def generate_model(model, seed):
    pass


def get_probability(model, word):
    pass
