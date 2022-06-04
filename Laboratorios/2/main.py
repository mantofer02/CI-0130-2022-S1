import sys
import parser_csv
import model


def main():
    n = 1
    decorator = '$'

    words = parser_csv.load_words('names.csv')
    words_with_decorators = parser_csv.add_decorators(
        words, decorator=decorator, n=n)

    sequences = parser_csv.get_sequences(words=words_with_decorators, n=n)
    model.calculate_transitions(
        words=words_with_decorators, sequences=sequences)


if __name__ == "__main__":
    main()
