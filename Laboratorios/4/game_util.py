
from unittest import result
from card import Card
import numpy as np

HAND_SIZE = 5
TIE = 0
PLAYER_WON = 1
OPPONENT_WON = -1
NOBODY_WON = -2


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

    result = win_by_royal_flush(
        player_numbers, player_symbols, opponent_numbers, opponent_symbols)

    if (result == PLAYER_WON):
        return True
    elif (result == OPPONENT_WON):
        return False

    result = win_by_straight_flush(
        player_numbers, player_symbols, opponent_numbers, opponent_symbols)

    if (result == PLAYER_WON):
        return True
    elif (result == OPPONENT_WON):
        return False

    result = win_by_four_of_a_kind(player_numbers, opponent_numbers)

    if (result == PLAYER_WON):
        return True
    elif (result == OPPONENT_WON):
        return False

    result = win_by_full_house(player_numbers, opponent_numbers)

    if (result == PLAYER_WON):
        return True
    elif (result == OPPONENT_WON):
        return False

    result = win_by_flush(player_numbers, player_symbols,
                          opponent_numbers, opponent_symbols)

    if (result == PLAYER_WON):
        return True
    elif (result == OPPONENT_WON):
        return False

    result = win_by_straight(player_numbers, opponent_numbers)

    if (result == PLAYER_WON):
        return True
    elif (result == OPPONENT_WON):
        return False

    result = win_by_three_of_a_kind(player_numbers, opponent_numbers)

    if (result == PLAYER_WON):
        return True
    elif (result == OPPONENT_WON):
        return False

    result = win_by_two_pair(player_numbers, opponent_numbers)

    if (result == PLAYER_WON):
        return True
    elif (result == OPPONENT_WON):
        return False

    result = win_by_one_pair(player_numbers, opponent_numbers)

    if (result == PLAYER_WON):
        return True
    elif (result == OPPONENT_WON):
        return False

    return get_high_card(player_numbers) > get_high_card(opponent_numbers)


def double_selection_sort(x: list[int], y: list[str]):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
        (y[i], y[swap]) = (y[swap], y[i])
    return x, y


def generic_tie_breaker(player_numbers, opponent_numbers):
    for i in range(len(player_numbers)):
        if player_numbers[i] > opponent_numbers[i]:
            return PLAYER_WON
        elif player_numbers[i] < opponent_numbers[i]:
            return OPPONENT_WON


def check_results(player_result, opponent_result):
    if (player_result == True and opponent_result == True):
        return TIE
    if (player_result):
        return PLAYER_WON

    if (opponent_result):
        return OPPONENT_WON

    return NOBODY_WON


def is_royal_flush(cards_numbers: list[int], cards_symbols: list[str]):
    value = 1 in cards_numbers and 11 in cards_numbers and 12 in cards_numbers and 13 in cards_numbers and 10 in cards_numbers and cards_symbols.count(
        cards_symbols[0]) == 5

    return value


def win_by_royal_flush(player_numbers: list[int], player_symbols, opponent_numbers: list[int], opponent_symbols):
    player_result = is_royal_flush(player_numbers, player_symbols)
    opponent_result = is_royal_flush(opponent_numbers, opponent_symbols)

    result = check_results(player_result, opponent_result)

    # No hay criterio de desempate, pero las probabilidades son bajas
    # entonces se asume que si hay empate gana el jugador
    if (result == TIE):
        return PLAYER_WON

    return result


def is_straight_flush(cards_numbers: list[int]):
    result = True
    cards_numbers.sort()
    for i in range(len(cards_numbers) - 1):
        if (cards_numbers[i] + 1 != cards_numbers[i + 1]):
            result = False
            break
    return result


def win_by_straight_flush(player_numbers, opponent_numbers):
    player_result = is_straight_flush(player_numbers)
    opponent_result = is_royal_flush(opponent_numbers)

    result = check_results(player_result, opponent_result)

    if (result == TIE):
        for i in range(len(player_numbers)):
            if player_numbers[i] > opponent_numbers[i]:
                return PLAYER_WON
            elif player_numbers[i] < opponent_numbers[i]:
                return OPPONENT_WON
    return result


def is_four_of_a_kind(cards_numbers: list[int]):
    cards_numbers.sort()
    if (cards_numbers.count([0]) == 4 or cards_numbers.count(cards_numbers[1]) == 4):
        return True
    return False


def win_by_four_of_a_kind(player_numbers, opponent_numbers):
    player_result = is_four_of_a_kind(player_numbers)
    opponent_result = is_four_of_a_kind(opponent_numbers)

    result = check_results(player_result, opponent_result)

    if (result == TIE):
        result = generic_tie_breaker(player_numbers, opponent_numbers)
    return result


def is_full_house(cards_numbers: list[int]):
    cards_numbers.sort()
    if (cards_numbers.count(cards_numbers[0]) == 3 and cards_numbers.count(cards_numbers[3]) == 2):
        return True
    elif (cards_numbers.count(cards_numbers[0]) == 2 and cards_numbers.count(cards_numbers[2]) == 3):
        return True
    return False


def win_by_full_house(player_numbers, opponent_numbers):
    player_result = is_full_house(player_numbers)
    opponent_result = is_full_house(opponent_numbers)

    result = check_results(player_result, opponent_result)

    if (result == TIE):
        result = generic_tie_breaker(player_numbers, opponent_numbers)

    return result


def is_flush(cards_symbols: list[str]):
    return cards_symbols.count(cards_symbols[0]) == HAND_SIZE


def win_by_flush(player_numbers, player_symbols, opponent_numbers, opponent_symbols):
    player_result = is_flush(player_symbols)
    opponent_result = is_flush(opponent_symbols)

    result = check_results(player_result, opponent_result)

    if (result == TIE):
        result = generic_tie_breaker(player_numbers, opponent_numbers)

    return result


def is_straight(cards_numbers: list[int], cards_symbols: list[str]):
    cards_numbers, cards_symbols = double_selection_sort(
        cards_numbers, cards_symbols)

    for i in range(len(cards_numbers) - 1):
        if not (cards_numbers[i] + 1 == cards_numbers[i + 1] and cards_symbols[i] != cards_symbols[i + 1]):
            return False
    return True


def win_by_straight(player_numbers, player_symbols, opponent_numbers, opponent_symbols):
    player_result = is_straight(player_numbers, player_symbols)
    opponent_result = is_straight_flush(opponent_numbers, opponent_symbols)

    result = check_results(player_result, opponent_result)

    if (result == TIE):
        result = generic_tie_breaker(player_numbers, opponent_numbers)

    return result


def is_three_of_a_kind(cards_numbers: list[int]):
    cards_numbers.sort()
    if (cards_numbers.count(cards_numbers[0]) == 3 or cards_numbers.count(cards_numbers[3]) == 3):
        return True
    return False


def win_by_three_of_a_kind(player_numbers, opponent_numbers):
    player_result = is_straight(player_numbers)
    opponent_result = is_straight_flush(opponent_numbers)

    result = check_results(player_result, opponent_result)

    if (result == TIE):

        highest_player = 0
        highest_opponent = 0

        for i in range(len(player_numbers)):
            if (player_numbers.count(player_numbers[i]) == 3):
                if (player_numbers[i] > highest_player):
                    highest_player = player_numbers[i]

            if (opponent_numbers.count(opponent_numbers[i]) == 3):
                if (opponent_numbers[i] > highest_opponent):
                    highest_opponent = opponent_numbers[i]

        if (highest_opponent > highest_player):
            return OPPONENT_WON
        elif (highest_opponent < highest_player):
            return PLAYER_WON

        highest_player = 0
        highest_opponent = 0

        for i in range(len(player_numbers)):
            if (player_numbers.count(player_numbers[i]) < 3):
                if (player_numbers[i] > highest_player):
                    highest_player = player_numbers[i]

            if (opponent_numbers.count(opponent_numbers[i]) < 3):
                if (opponent_numbers[i] > highest_opponent):
                    highest_opponent = opponent_numbers[i]

        if (highest_opponent > highest_player):
            return OPPONENT_WON
        else:
            return PLAYER_WON

    return result


def is_two_pair(cards_numbers: list[int]):
    cards_numbers.sort()
    for i in range(len(cards_numbers) - 1):
        if (cards_numbers.count(cards_numbers[i]) == 2):
            if i + 3 < len(cards_numbers):
                if (cards_numbers.count(cards_numbers[i + 2]) == 2 or cards_numbers.count(cards_numbers[i + 3]) == 2):
                    return True
    return False


def win_by_two_pair(player_numbers, opponent_numbers):
    player_result = is_two_pair(player_numbers)
    opponent_result = is_two_pair(opponent_numbers)

    result = check_results(player_result, opponent_result)

    if (result == TIE):
        result = generic_tie_breaker(player_numbers, opponent_numbers)

    return result


def is_one_pair(cards_numbers: list[int]):
    cards_numbers.sort()
    for i in range(len(cards_numbers)):
        if (cards_numbers.count(cards_numbers[i]) == 2):
            return True
    return False


def win_by_one_pair(player_numbers, opponent_numbers):
    player_result = is_one_pair(player_numbers)
    opponent_result = is_one_pair(opponent_numbers)

    result = check_results(player_result, opponent_result)

    if (result == TIE):
        result = generic_tie_breaker(player_numbers, opponent_numbers)

    return result


def get_high_card(cards_numbers: list[int]):
    cards_numbers.sort()
    return cards_numbers[-1]
