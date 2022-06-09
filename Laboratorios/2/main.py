import sys
import parser_csv
import model


def main():
    words = parser_csv.load_words('pokemon.csv')
    my_model = model.create_model(words=words, ngrams=3)
    print(model.generate_word(my_model, 21))


if __name__ == "__main__":
    main()
