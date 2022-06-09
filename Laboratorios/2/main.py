import sys
import parser_csv
import model


def main():
    words = parser_csv.load_words('pokemon.csv')
    n_gram_model = model.Model()
    my_model = n_gram_model.create_model(words=words, ngrams=3)
    print(n_gram_model.generate_word(my_model, 21))


if __name__ == "__main__":
    main()
