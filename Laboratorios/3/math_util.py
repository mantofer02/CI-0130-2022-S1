import random
import math
from numpy import log as ln

"""
    @function
    rand_exp
    @description
    Function that creates a random value following an exponencial distribution
    ----------
    @parameters
    ----------
    lambd:  int
            integer number that is used as a lambda value.
"""


def rand_exp(lambd):
    value = -ln(1 - random.uniform(0, 1)) / lambd
    return value


"""
    @function
    lambd
    @description
    Function that returns a lambda value.
    ----------
    @parameters
    ----------
    n:  int
            integer number that represents the ammount of clients.
"""


def lambd(n):
    return 64 - (n**1.5)


"""
    @function
    mu
    @description
    Function that returns a mu value.
    ----------
    @parameters
    ----------
    n:  int
            integer number that represents the ammount of clients.
"""


def mu(n):
    value = 5 + (3*n)
    if (value == 0):
        print("soy gay")
        input()
    return 5 + (3*n)
