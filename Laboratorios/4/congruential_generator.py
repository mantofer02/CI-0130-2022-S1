import time


class CongrentualGenerator:
    def __init__(self, a, b, m) -> None:
        self.a = a
        self.b = b
        self.m = m
        self.x = time.time()*1000

    def seed(self, s):
        self.x = s

    def random(self):
        self.x = (self.a*self.x + self.b) % self.m
        return self.x / self.m

    def period(self):
        x = 0
        results = []
        counter = 0
        x_n = (self.a*x + self.b) % self.m
        while (not x_n in results):
            results.append(x_n)
            x = x_n
            x_n = (self.a*x + self.b) % self.m
            counter += 1
        return counter
