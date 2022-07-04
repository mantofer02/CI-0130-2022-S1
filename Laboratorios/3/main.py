import math_util
from queue import Queue


def main():
    myQeue = Queue(lmax=2, s=3, lambd=math_util.lambd, mu=math_util.mu)


if __name__ == "__main__":
    main()
