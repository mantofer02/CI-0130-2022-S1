
from congruential_generator import CongruentialGenerator
from card import Card
import random_util
import game_util


def main():
    abm = random_util.good_abm(10000000)

    random_generator = CongruentialGenerator(a=abm[0], b=abm[1], m=abm[2])
    print("a value: " + str(abm[0]))
    print("b value: " + str(abm[1]))
    print("m value: " + str(abm[2]))
    print("period value: " + str(random_generator.period()))

    stack = game_util.generate_cards_stack()
    player_cards_numbers = []

    for i in range(2):
        index = int(random_generator.random() * len(stack))
        player_cards_numbers.append(index)
        stack.pop(index)

    results = game_util.simulate(
        player_cards_numbers, 100000, random_generator)
    print("Test case 1: ")
    print("Wins %: " + str(results[0] * 100))
    print("Lose %: " + str(results[2] * 100))

    stack = game_util.generate_cards_stack()
    player_cards_numbers = []

    for i in range(2):
        index = int(random_generator.random() * len(stack))
        player_cards_numbers.append(index)
        stack.pop(index)

    print()
    results = game_util.simulate(
        player_cards_numbers, 100000, random_generator)
    print("Test case 2: ")
    print("Wins %: " + str(results[0] * 100))
    print("Lose %: " + str(results[2] * 100))

    stack = game_util.generate_cards_stack()
    player_cards_numbers = []

    for i in range(2):
        index = int(random_generator.random() * len(stack))
        player_cards_numbers.append(index)
        stack.pop(index)

    print()
    results = game_util.simulate(
        player_cards_numbers, 100000, random_generator)
    print("Test case 3: ")
    print("Wins %: " + str(results[0] * 100))
    print("Lose %: " + str(results[2] * 100))


if __name__ == "__main__":
    main()
