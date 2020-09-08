class BlackJack(object):
    """
    setup the rule of blackjack
    """

    RANKS = (*"A23456789", "10", *"JQK")
    values = list(range(1,11))
    # values are card pure values
    values.extend([10, 10, 10])
    # let ranks and values align with tuple
    VALUES = (values)
    RANK_TO_VALUES = dict(zip(RANKS, VALUES))



