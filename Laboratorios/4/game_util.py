
from card import Card
import numpy as np
HAND_SIZE = 5


def generate_cards_stack():
    symbols = ['D', 'H', 'S', 'T']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    stack = []

    for i in range(len(numbers)):
        for j in symbols:
            stack.append(Card(numbers[i], j))

    return stack


def compare_hands(player: list[Card], opponent: list[Card]):
    player_numbers = []
    player_symbols = []

    opponent_numbers = []
    opponent_symbols = []

    player_round = False
    opponent_round = False

    for i in player:
        player_numbers.append(i.number)
        player_symbols.append(i.symbol)

    for i in opponent:
        opponent_numbers.append(i.number)
        opponent_symbols.append(i.symbol)

    player_numbers, player_symbols = double_selection_sort(
        player_numbers, player_symbols)

    opponent_numbers, opponent_symbols = double_selection_sort(
        opponent_numbers, opponent_symbols)

    player_round = is_royal_flush(player_numbers)
    opponent_round = is_royal_flush(opponent_numbers)

    if (opponent_round == player_round):
        player_round = False
        opponent_round = False
    elif (opponent_round == True):
        return False
    else:
        return True

    player_round = is_straight_flush(player_numbers)
    opponent_round = is_straight_flush(opponent_numbers)

    if (opponent_round == player_round):
        player_round = False
        opponent_round = False
    elif (opponent_round == True):
        return False
    else:
        return True

    player_round = is_four_of_a_kind(player_numbers)
    opponent_round = is_four_of_a_kind(opponent_numbers)

    if (opponent_round == player_round):
        player_round = False
        opponent_round = False
    elif (opponent_round == True):
        return False
    else:
        return True

    player_round = is_full_house(player_numbers)
    opponent_round = is_full_house(opponent_numbers)

    if (opponent_round == player_round):
        player_round = False
        opponent_round = False
    elif (opponent_round == True):
        return False
    else:
        return True

    player_round = is_flush(player_symbols)
    opponent_round = is_flush(opponent_symbols)

    if (opponent_round == player_round):
        player_round = False
        opponent_round = False
    elif (opponent_round == True):
        return False
    else:
        return True

    player_round = is_straight(player_numbers, player_symbols)
    opponent_round = is_straight(opponent_numbers, opponent_symbols)

    if (opponent_round == player_round):
        player_round = False
        opponent_round = False
    elif (opponent_round == True):
        return False
    else:
        return True

    player_round = is_three_of_a_kind(player_numbers)
    opponent_round = is_three_of_a_kind(opponent_numbers)

    if (opponent_round == player_round):
        player_round = False
        opponent_round = False
    elif (opponent_round == True):
        return False
    else:
        return True

    player_round = is_two_pair(player_numbers)
    opponent_round = is_two_pair(opponent_numbers)

    if (opponent_round == player_round):
        player_round = False
        opponent_round = False
    elif (opponent_round == True):
        return False
    else:
        return True

    player_round = is_one_pair(player_numbers)
    opponent_round = is_one_pair(opponent_numbers)

    if (opponent_round == player_round):
        player_round = False
        opponent_round = False
    elif (opponent_round == True):
        return False
    else:
        return True

    return get_high_card(player_numbers) > get_high_card(opponent_numbers)


def is_royal_flush(cards_numbers: list[int]):
    return 1 in cards_numbers and 11 in cards_numbers and 12 in cards_numbers and 13 in cards_numbers and 10 in cards_numbers


def is_straight_flush(cards_numbers: list[int]):
    result = True
    cards_numbers.sort()
    for i in range(len(cards_numbers) - 1):
        if (cards_numbers[i] + 1 != cards_numbers[i + 1]):
            result = False
            break
    return result


def is_four_of_a_kind(cards_numbers: list[int]):
    cards_numbers.sort()
    if (cards_numbers.count([0]) == 4 or cards_numbers.count(cards_numbers[1]) == 4):
        return True
    return False


def is_full_house(cards_numbers: list[int]):
    cards_numbers.sort()
    if (cards_numbers.count(cards_numbers[0]) == 3 and cards_numbers.count(cards_numbers[3]) == 2):
        return True
    elif (cards_numbers.count(cards_numbers[0]) == 2 and cards_numbers.count(cards_numbers[2]) == 3):
        return True
    return False


def is_flush(cards_symbols: list[str]):
    return cards_symbols.count(cards_symbols[0]) == HAND_SIZE


def is_straight(cards_numbers: list[int], cards_symbols: list[str]):
    cards_numbers, cards_symbols = double_selection_sort(
        cards_numbers, cards_symbols)

    for i in range(len(cards_numbers) - 1):
        if not (cards_numbers[i] + 1 == cards_numbers[i + 1] and cards_symbols[i] != cards_symbols[i + 1]):
            return False
    return True


def double_selection_sort(x: list[int], y: list[str]):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
        (y[i], y[swap]) = (y[swap], y[i])
    return x, y


def is_three_of_a_kind(cards_numbers: list[int]):
    cards_numbers.sort()
    if (cards_numbers.count(cards_numbers[0]) == 3 or cards_numbers.count(cards_numbers[3]) == 3):
        return True
    return False


def is_two_pair(cards_numbers: list[int]):
    cards_numbers.sort()
    for i in range(len(cards_numbers) - 1):
        if (cards_numbers.count(cards_numbers[i]) == 2):
            if i + 3 < len(cards_numbers):
                if (cards_numbers.count(cards_numbers[i + 2]) == 2 or cards_numbers.count(cards_numbers[i + 3]) == 2):
                    return True
    return False


def is_one_pair(cards_numbers: list[int]):
    cards_numbers.sort()
    for i in range(len(cards_numbers)):
        if (cards_numbers.count(cards_numbers[i]) == 2):
            return True
    return False


def get_high_card(cards_numbers: list[int]):
    cards_numbers.sort()
    return cards_numbers[-1]


print(is_two_pair([2, 2, 4, 5, 5]))
