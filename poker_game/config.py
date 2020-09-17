class SetOfCard(object):
    # Mark
    MARKS = ("♠︎", "❤︎", "♦︎", "♣️")
    # priority display
    # ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    RANKS = (*"A23456789", "10", *"JQK")
    # priority number
    NUMBERS = list(range(1, 11))
    NUMBERS.extend([10, 10, 10])
    # combine mark and number
    NUMBER_TO_RANK = dict(zip(NUMBERS, RANKS))
    RANK_TO_NUMBER = dict(zip(RANKS, NUMBERS))
    # {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
    #  7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}