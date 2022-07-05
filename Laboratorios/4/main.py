
from congruential_generator import CongrentualGenerator
import random_util


def main():
    abm = random_util.good_abm(10)
    myRandom = CongrentualGenerator(a=abm[0], b=abm[1], m=abm[2])


if __name__ == "__main__":
    main()
