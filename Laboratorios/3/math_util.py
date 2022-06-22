import random
from numpy import log as ln


def rand_exp(lambd):
    value = -ln(1 - random.uniform(0, 1)) / lambd
    return value
