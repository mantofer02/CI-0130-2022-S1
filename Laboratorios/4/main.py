
from congruential_generator import CongruentialGenerator
from card import Card
import random_util
import game_util


def main():
    abm = random_util.good_abm(200)
    random_generator = CongruentialGenerator(a=abm[0], b=abm[1], m=abm[2])
    print("m value: " + str(abm[1]))
    print("period value: " + str(random_generator.period()))

    stack = game_util.generate_cards_stack()
    player_cards: list[Card] = []

    for i in range(2):
        player_cards.append(
            stack.pop(int(random_generator.random() * len(stack))))

    results = game_util.simulate(player_cards, 40, random_generator)
    print(results)


if __name__ == "__main__":
    main()
