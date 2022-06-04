
import numpy as np


def calculate_transitions(words, sequences):
    prob_matrix = np.zeros(shape=(len(sequences), len(sequences)))
    prob_matrix.dtype = np.dtype(np.float64)

    print(prob_matrix.dtype)


def create_model(words, ngrams):
    pass


def generate_model(model, seed):
    pass


def get_probability(model, word):
    pass
