import random
import math
from numpy import log as ln


def rand_exp(lambd):
    value = -ln(1 - random.uniform(0, 1)) / lambd
    return value


def lambd(n):
    return 64 - (n**1.5)


def mu(n):
    return 5 + (3*n)
