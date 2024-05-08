# cards dictionary
cards_dict = {
    'S2': 2,
    'S3': 3,
    'S4': 4,
    'S5': 5,
    'S6': 6,
    'S7': 7,
    'S8': 8,
    'S9': 9,
    'S10': 10,
    'SJ': 11,
    'SQ': 12,
    'SK': 13,
    'SA': 14
}


# create functions that can later be tested
def check_straight(card1, card2, card3):
    cards = [card1, card2, card3]
    # sort cards in ascending order
    cards.sort(key=cards_dict.get)  # cards_dict.get calls values from the cards dictionary

    # check to see if cards are in sequential order
    if cards_dict[cards[0]] == cards_dict[cards[1]] - 1 == cards_dict[cards[2]] - 2:
        # return greatest value
        return cards_dict[cards[2]]
    else:
        # return 0 if not in sequence
        return 0


# create check_3ofa_kind function
def check_3ofa_kind(card1, card2, card3):
    # compares cards using cards dictionary to see if they are all the same 
    if cards_dict[card1] == cards_dict[card2] == cards_dict[card3]:
        return cards_dict[card1]
    else:
        # return 0 if not 3 of a kind
        return 0


# create check_royal_flush function
def check_royal_flush(card1, card2, card3):
    # pulling from check_straight function. If in order and greatest value = 14 then it's a royal flush
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0


def play_cards(left1, left2, left3, right1, right2, right3):
    # split up cards with left and right list so we can compare the two
    left_cards = [left1, left2, left3]
    right_cards = [right1, right2, right3]

    left_straight = check_straight(*left_cards)
    right_straight = check_straight(*right_cards)

    left_3ofa_kind = check_3ofa_kind(*left_cards)
    right_3ofa_kind = check_3ofa_kind(*right_cards)

    left_royal_flush = check_royal_flush(*left_cards)
    right_royal_flush = check_royal_flush(*right_cards)

    # checking for royal_flush
    if left_royal_flush and not right_royal_flush:
        return -1
    elif right_royal_flush and not left_royal_flush:
        return 1

    # checking who wins if straight
    elif left_straight and right_straight:
        if left_straight > right_straight:
            return -1
        elif left_straight < right_straight:
            return 1
        else:
            return 0

    # checking if one player plays straight and other plays 3 of a kind. Straight wins regardless
    elif left_straight and right_3ofa_kind:
        return -1
    elif right_straight and left_3ofa_kind:
        return 1

    # checking if left and right are 3 of a kind
    elif left_3ofa_kind and right_3ofa_kind:
        if left_3ofa_kind > right_3ofa_kind:
            return -1
        elif left_3ofa_kind < right_3ofa_kind:
            return 1
        else:
            return 0
    else:
        return 0
