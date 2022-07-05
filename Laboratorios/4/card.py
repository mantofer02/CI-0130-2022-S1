

class Card:
    def __init__(self, number: int, symbol: str) -> None:
        self.number = number
        self.symbol = symbol

    def print_card(self):
        print("[ " + str(self.number) + " " + str(self.symbol) + " ]")
