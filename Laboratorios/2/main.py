import sys
import parser_csv


def main():
    # parser_csv.load_words('pokemon.csv')
    #print(parser_csv.add_decorators(parser_csv.load_words('pokemon.csv'), "$", 2))
    print(parser_csv.get_sequences(parser_csv.add_decorators(
        parser_csv.load_words('pokemon.csv'), "$", 2), 3))
    pass


if __name__ == "__main__":
    main()
