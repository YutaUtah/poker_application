from poker_game.config import SetOfCard

class Card(SetOfCard):
    """
    mark and number input in Card

    Attributes
    ----------
    card_mark : int
        mark（♠︎❤︎♦︎♣️）
    card_number : int
        card number
    """
    def __init__(self, card_mark, card_number):
        """
        Parameters
        ----------
        card_mark : int
            mark（♠︎❤︎♦︎♣️）
        card_number : int
            number
        """
        self.mark = card_mark
        self.number = card_number
        self.rank = self.NUMBER_TO_RANK[self.number]
        self.pair = f"{self.MARKS[self.mark]}-{self.rank}"

    def __repr__(self):
        """
        change instance input override

        Returns
        -------
        combined mark and number str output

        Examples
        --------
        >>> card = Card(2, 4)
        >>> print(card)
        ♦︎4
        """
        return self.pair




