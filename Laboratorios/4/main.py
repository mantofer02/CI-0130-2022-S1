
from congruential_generator import CongrentualGenerator


def main():
    myRandom = CongrentualGenerator(a=52, b=19, m=17)
    print(myRandom.period())


if __name__ == "__main__":
    main()
