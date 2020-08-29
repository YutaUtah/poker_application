class Card:
    """
    mark and number input in Card

    Attributes
    ----------
    card_mark : int
        mark（♠︎❤︎♦︎♣️）
    card_number : int
        card number
    """

    # Mark
    MARKS = ("♠︎", "❤︎", "♦︎", "♣️")
    # priority display
    # ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    RANKS = (*"A23456789", "10", *"JQK")
    # priority number
    NUMBERS = (range(1, 13 + 1))
    # combine mark and number
    NUMBER_TO_RANK = dict(zip(NUMBERS, RANKS))

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


# Cardクラスからインスタンスを生成（引数にマークと数字）
# reprメソッドで出力内容を変更しているので下記のように出力される
# 通常 → <__main__.Card object at 0x10c949310>
# reprメソッド追加 → ♦︎-4

if __name__ == '__main__':
    card = Card(2, 12)
    print(card.number)
    print(card.NUMBER_TO_RANK)
