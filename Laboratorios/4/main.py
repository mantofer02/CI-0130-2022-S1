
from congruential_generator import CongruentialGenerator
from card import Card
import random_util
import game_util


def generate_cards_stack():
    symbols = ['D', 'H', 'S', 'T']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    stack = []

    for i in range(len(numbers)):
        for j in symbols:
            stack.append(Card(numbers[i], j))

    return stack


def main():
    abm = random_util.good_abm(100000000)
    print(abm)
    input()
    random_generator = CongruentialGenerator(a=abm[0], b=abm[1], m=abm[2])

    stack = generate_cards_stack()
    player_cards: list[Card] = []
    opponent_cards: list[Card] = []

    for i in range(7):
        random_generator.random() * len(stack)


        # print(int(random_generator.random() * len(stack)))
        # player_cards.append(
        #     stack.pop(int(random_generator.random() * len(stack))))
        # opponent_cards.append(
        #     stack.pop(int(random_generator.random() * len(stack))))
        # print("Player cards: ")
        # for i in player_cards:
        #     i.print_card()
        # print()
        # print("Opponent cards: ")
        # for i in opponent_cards:
        #     i.print_card()
        # print()
if __name__ == "__main__":
    main()
