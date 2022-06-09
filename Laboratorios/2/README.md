# CI-0130-2022-S1 | Laboratory 2

This project was developed by:

**B82957** | Marco Ferraro Rodriguez <br>
**B71146** | Gabriel Bogantes Armijo

- [CI-0130-2022-S1 | Laboratory 2](#ci-0130-2022-s1--laboratory-2)
- [Incremention of probability if "n" becomes bigger](#why-does-the-probability-of-forming-a-name-seems-to-increment)
- [Interesting Pokemon name](#did-you-find-any-other-interesting-name-for-a-pokemon-what-was-the-value-of-n-and-its-seed-did-you-find-a-name-that-doesnt-make-any-sense-include-the-code-used)
- [Pokemon name that doesn't make sense](#did-you-find-any-other-interesting-name-for-a-pokemon-what-was-the-value-of-n-and-its-seed-did-you-find-a-name-that-doesnt-make-any-sense-include-the-code-used)
- [Explanation for the use of Markov Chains in this Laboratory](#explain-in-your-own-words-in-which-way-are-the-markov-chains-being-used-to-modulate-the-names)

## Why does the probability of forming a name seems to increment?

<p>The probability increments because of a very simple reason. When the size for the diverse sequences increments, it is more probable for it to be in the transition matrix. This means that the longer the sequence, the easier for it to be part of the word. Also, it becomes bigger because when it looks for a specific sequence, there are less multiplications that would make it less possible.</p>

## Did you find any other interesting name for a Pokemon? What was the value of n and it's seed? Did you find a name that doesn't make any sense? Include the code used. 

<li>We found an interesting name because it has a similar name to a town in Germany, the name for the city was St. Angela whereas we generated the name Stangela. For this name we used ngram = 3 and the seed = 0.  </li>

<p>For running the interesting name change the main for the following:</p>
<code>
    def main():
    words = parser_csv.load_words('pokemon.csv')<br>
    n_gram_model = model.Model()<br>
    my_model = n_gram_model.create_model(words=words, ngrams=3)<br>
    print(n_gram_model.generate_word(my_model, 0))
</code>


<li>We found a name that doesn't make any sense with the n-gram size of 2 and the seed 69. It was "Racnettongdrang". </li>

<p>For running the weird name change the main for the following:</p>
<code>
    def main():
    words = parser_csv.load_words('pokemon.csv')<br>
    n_gram_model = model.Model()<br>
    my_model = n_gram_model.create_model(words=words, ngrams=2)<br>
    print(n_gram_model.generate_word(my_model, 69))
</code>


## Explain in your own words, in which way are the Markov Chains being used to modulate the names?

<p>They are being used because Markov Chains are basically a model to store probabilities and use them in the future. Every transition matrix modifies itself depending on the times they are being multiplied. The interesting thing behind it is that there is a point where all the values tend to a specific number. They are being used by randomly reaching cell's. When it is a valid cell it stores it into a string until it reaches the ending point.</p>
