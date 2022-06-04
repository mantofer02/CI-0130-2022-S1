import sys
import parser_csv


def main():
    n = 3
    print(parser_csv.get_sequences(parser_csv.add_decorators(
        parser_csv.load_words('test.csv'), "$", n), n))
    pass


if __name__ == "__main__":
    main()
