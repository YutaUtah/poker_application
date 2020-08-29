class Player(object):
    def keep_drawing_card(self):
        """
        playerに hit or stand 決めさせる
        （stand で player のターンが終了）
        Parameters
        ----------
        deck : deck
            カードひと組
        """
        pass

    def draw_card(self):
        """
        カードをデッキからドローし手札に加える
        ※異なる枚数がドローされてもok
        Parameters
        ----------
        num : int, default 1
            カードをドローする回数
        Examples
        --------
        >>> player.draw_card(2) # 2枚ドロー [♠︎-J, ♠︎-10]
        >>> player.draw_card(3) # [♦︎-9, ♣️-10, ♠︎-2]
        >>> print(player.hands)
        [♠︎-J, ♠︎-10, ♦︎-9, ♣️-10, ♠︎-2]
        """
        pass

class Dealer(object):

    def keep_drawing_card(self):
        """
        dealerは17超えるまで自動でカードを引き続ける
        17超えたら終了
        Parameters
        ----------
        deck : object
            現在の手札
        """
        pass

