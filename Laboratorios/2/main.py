import sys
import parser_csv
import model


def main():
    n = 3
    seed = 21

    words = parser_csv.load_words('pokemon.csv')
    n_gram_model = model.Model()
    my_model = n_gram_model.create_model(words=words, ngrams=n)

    print("Word generated with " + str(n) +
          " n grams and a seed value of " + str(seed) + ": ")
    print("\t" + str(n_gram_model.generate_word(model=my_model, seed=seed)))

    print()
    word_to_search = "mew"
    print("Probability of obtaining the word " +
          word_to_search + " in said model:")
    print("\t" + str(n_gram_model.get_probability(model=my_model, word=word_to_search)))


if __name__ == "__main__":
    main()
