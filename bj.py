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

    @classmethod
    def calculate_current_score(cls, person):
        person.current_score()
        person.curent_sub_score()
        person.has_A = False

        for card in person.hands:
            card_rank = str(card).split("-")[1]
            card_value = cls.RANK_TO_VALUES[card_rank]


