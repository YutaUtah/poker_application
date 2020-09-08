# card class
from poker_game.card import Card

from random import shuffle

class Deck(object):
    """
    attribute
    ---------
    deck_num: the number of deck(each contains 52)

    all_cards: all cards with mark and value in n decks
    """

    def __init__(self, deck_num=1):
        self.deck_num = deck_num
        self.all_cards = []

        for deck in range(self.deck_num):
            for mark in range(0,len(Card.MARKS)):
                for value in Card.NUMBERS:
                    self.all_cards.append(Card(mark, value))

        shuffle(self.all_cards)

    def pick_card(self, draw_num):
        """

        :param draw_num:
        :return: designated cards we drew, should return the list
        """
        self.draw_card = []
        if draw_num == 0:
            return self.all_cards
        else:
            for draw in range(draw_num):
                self.draw_card.append(self.all_cards.pop())


        return self.draw_card


"""
Deck(2) means that there are two decks and deck object is the aggragate of these
card_left is the decks - draw_card
"""



if __name__ == "__main__":
    deck = Deck(2)
    print(deck.pick_card(5))


