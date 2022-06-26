from server import Server
from client import Client


class Queue:
    # lambd and mu are function
    def __init__(self, lmax, s, lambd, mu) -> None:
        self.lmax = lmax
        self.s = s
        self.lambd = lambd
        self.mu = mu
        print(self.s)
        pass

    def simulation(self, time_limit):
        pass
