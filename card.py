class Card(object):
    """
    attribute
    ---------
    my_mark represents 4 card marks: spades, hearts, diamonds, and clubs

    card_value represents value of cards from ace(1) to king(13)
    """

    MARKS = ["♠︎-", "❤︎-", "♦︎-", "♣️-"]
    VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def __init__(self, my_mark, my_value):
        self.mark = my_mark
        self.value = my_value

    def __repr__(self):
        return self.MARKS[self.mark] + str(self.VALUES[self.value-1])


card = Card(1,10)

