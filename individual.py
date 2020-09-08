from deck import Deck

class Player:
    """
    Player class

    instantiate:
    win count to be 0
    hands list to be empty
    current score to be 0
    current score sub to be 0
    has A card to be False boolean
    """

    def __init__(self):
        self.win_count = 0
        self.hands = []
        self.current_score = 0
        self.current_sub_score = 0
        self.has_A = False

    def keep_drawing_card(self, deck):
        """
        playerに hit or stand 決めさせる
        （stand で player のターンが終了）

        Parameters
        ----------
        deck : deck
            カードひと組
        """
        draw_card_or_not = True
        while draw_card_or_not:
            hit_or_stand_msg = "\nHit(1) or Stand(2) : "
            hit_or_stand_response = input("\nHit(1) or Stand(2) : ")
            if hit_or_stand_response == 1:
                # this is hit, draw one card from decks
                self.draw_card(deck)
                BlackJack.calculate_current_score()
                pass
                # self.draw_card(deck)
            if hit_or_stand_response == 2:
                pass

    def draw_card(self, deck, num=1):
        """
        add card from deck to yours
        ※異なる枚数がドローされてもok

        Parameters
        ----------
        num : int, default 1
            カードをドローする回数

        """
        self.hands_store = deck.pick_card(num)
        self.hands.extend(self.hands_store)

