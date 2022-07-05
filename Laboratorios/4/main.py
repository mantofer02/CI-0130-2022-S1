
from congruential_generator import CongrentualGenerator
import random_util
import game_util


def main():
    abm = random_util.good_abm(10)
    myRandom = CongrentualGenerator(a=abm[0], b=abm[1], m=abm[2])

    stack = game_util.generate_cards_stack()
    for i in stack:
        i.print_card()


if __name__ == "__main__":
    main()
