import numpy as np
import random

# DECORATOR = "$"


class Model:
    def __init__(self) -> None:
        # Default values n
        self.decorator = "$"
        self.n = 1
    """
        @function
        create_model
        @description
        Model that unifies the following functions into one: add_decorators(), get_sequences(), and calculate_transitions()
        ----------
        @parameters
        ----------
        words : str array
            Array that contains all the parsed words.
        n : int
            Expected size of the n-gram.
    """

    def create_model(self, words, ngrams):
        decorator = '$'

        words_with_decorators = self.add_decorators(
            words, decorator=decorator, n=ngrams)

        sequences = self.get_sequences(words=words_with_decorators, n=ngrams)
        transition = self.calculate_transitions(
            words=words_with_decorators, sequences=sequences)

        return transition, sequences
    """
        @function
        add_decorators
        @description
        Returns a string array with the modified words concatenated with the decorator.
        ----------
        @parameters
        ----------
        words : str array
            Array that contains all the parsed words.
        decorator : char
            Char that is going to be concatenated to every word.
        n : int
            Ammount of chars to be added to every word on each side.
    """

    def add_decorators(self, words, decorator, n):
        self.decorator = decorator
        self.n = n

        concatenate_string = self.decorator * self.n
        for index in range(len(words)):
            words[index] = concatenate_string + \
                words[index].lower() + concatenate_string
        return(words)
    """
            @function
            calculate_transitions
            @description
            Returns a  probability matrix with all possible ocurrences in each 
            word and sequence comparisson. 
            ----------
            @parameters
            ----------
            words : str array
                Array that contains all the parsed and decorated words.
            sequences : str array
                Array that contains all the possible combinations for sequences. 
    """

    def calculate_transitions(self, words, sequences):
        prob_matrix = np.zeros(shape=(len(sequences), len(sequences)))
        prob_matrix.dtype = np.dtype(np.float64)

        for i in range(len(sequences)):
            counter = 0
            for element in words:
                index = element.find(sequences[i])
                if index != -1:
                    for j in range(len(sequences)):
                        if (element[index + 1: index + 1 + self.n] == sequences[j]):
                            prob_matrix[i][j] += 1
                            counter += 1
            if counter != 0:
                prob_matrix[i][:] = prob_matrix[i][:] / counter
        return prob_matrix

    """
        @function
        get_sequences
        @description
        Returns a string array with all the possible sequences.
        ----------
        @parameters
        ----------
        words : str array
            Array that contains all the parsed words.
        n : int
            Length of expected sequences to be created. 
    """

    def get_sequences(self, words, n):
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

    """
        @function
        generate_word
        @description
        Returns a word depending on the seed number and the model previously defined.
        ----------
        @parameters
        ----------
        model : tuple
            Tuple that contains transitions matrix and sequences array.
        seed : int
            Integer number that contains the prefered seed to run the algorithm.
    """

    def generate_word(self, model, seed):

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

        return word.replace(self.decorator, "").capitalize()
    """
        @function
        get_probability 
        @description
        Returns a word depending on the seed number and the model previously defined.
        ----------
        @parameters
        ----------
        model : tuple
            Tuple that contains transitions matrix and sequences array.
        seed : int
            Integer number that contains the prefered seed to run the algorithm.
    """

    def get_probability(self, model, word):
        prob_matrix = model[0]
        sequences = model[1]

        word = word.lower()
        concatenate_string = self.decorator * len(sequences[0])
        word = concatenate_string + word + concatenate_string

        probability = float(0)

        for i in range(len(sequences)):
            index = word.find(sequences[i])
            if index != -1:
                for j in range(len(sequences)):
                    if (word[index + 1: index + 1 + self.n] == sequences[j]):
                        if probability == float(0):
                            probability += prob_matrix[i][j]
                        else:
                            probability = probability * prob_matrix[i][j]
        return probability
