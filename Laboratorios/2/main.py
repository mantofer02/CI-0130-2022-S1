import sys
import parser_csv
import model
import random


def main():
    words = parser_csv.load_words('test.csv')
    my_model = model.create_model(words=words, ngrams=1)
    print(model.generate_word(my_model, 17))


if __name__ == "__main__":
    main()
