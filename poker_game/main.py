from deck import Deck
from card import Card


# todo: why does display_cards does not work if i use this function above the function?




def start_game():
    """
    Start a poker game.

    When this function is called,
    Display User's two cards from a deck and dealer's card,
    provide a choice to user whether he will take a new card,
    if the sum of number goes above 21, close the game (application),
    as long as the sum is less than 21, the choice to take another card will be provided,
    once the user choose not to draw a card, the dealer will draw a card as long as the sum is less than 18,
    if the sum of number of dealer cards goes above 21, the user will win,
    once the dealer stops drawining a card without the number going above 21,
    will check whether user or dealer has a closer number of sum to 21.

    Returns:
        None
    """
    deck = Deck()

    user_cards = deck.pick_card(2)
    dealer_cards = deck.pick_card(2)

    """
    Examples:
    user_cards = {"displayed":[6, 11], "hidden": []}
    dealer_cards = {"displayed":[8], "hidden": [12]}
    """

    # todo: without return value on this function, how does it work?
    # display_cards(user_cards, dealer_cards)
    # user_cards = user_decide_draw_cards(user_cards, deck)

    user_cards, dealer_cards = display_cards(user_cards, dealer_cards)
    user_cards = user_decide_draw_cards(user_cards, deck)
    a = dealer_draw_cards(dealer_cards, deck)
    user_card_sum = check_the_sum(user_cards, dealer_cards, deck)







    # if check_the_sum(user_cards) > 21:
    #     return 0
    #
    # dealer_cards = deader_draw_cards(dealer_cards, deck)
    #
    # if check_the_sum(dealer_cards) > 21:
    #     return 1
    #
    # results = check_who_wins(user_cards, dealer_cards)
    #
    # return results


# def draw_two_cards_from_deck(deck):
#     """
#     Draw two cards for users and dealers from deck object.
#
#     Write a description of this function in details.
#
#     Args:
#         deck: a card deck object
#
#     Returns:
#         two dictionaries with keys displayed and hidden
#     """
#     #TODO: Please write a logic
#
#     return user_cards, dealer_cards


def display_cards(user_cards, dealer_cards):
    """
    Wriate a short summary of this function

    Write a description of this function in details.

    Args:
        user_cards:
        dealer_cards:

    Returns:
        None
    """
    # TODO: Please write a logic
    keyDict_user = {"displayed", "hidden"}
    keyDict_dealer = {"displayed", "hidden"}
    game_card_user = dict([(key, []) for key in keyDict_user])
    game_card_dealer = dict([(key, []) for key in keyDict_dealer])
    game_card_user["displayed"] = user_cards
    game_card_dealer["displayed"], game_card_dealer["hidden"] = [dealer_cards[0]], [dealer_cards[1]]

    print("Your cards:")
    print(game_card_user["displayed"])

    print("Dealer card: ")
    print(game_card_dealer["displayed"])

    return game_card_user, game_card_dealer


def user_decide_draw_cards(game_card_user, deck):
    """
    Write a short summary of this function

    Write a description of this function in details.

    Args:
        game_card_user:
        deck:

    Returns:
        game_card_user
    """
    # TODO: Please write a logic

    decided = False
    while decided is False:
        draw_or_not = input("You have 2 cards {}. Do you want to draw 1 more card? [y/n] \n".format(game_card_user["displayed"]))

        if draw_or_not == 'y':
            user_next_card = deck.pick_card(1)
            game_card_user["displayed"].append(user_next_card[0])
            decided = True
        elif draw_or_not == 'n':
            decided = True
            pass
        else:
            print("Please input appropriate answer!")

    print("your current cards are {}".format(game_card_user["displayed"]))



    return game_card_user


def check_the_sum(user_cards, dealer_cards, deck):
    """
    Wriate a short summary of this function

    Write a description of this function in details.

    Args:
        user_cards:
        dealer_cards:
        deck:

    Returns:
        None
    """
    # TODO: Please write a logic (what happens if i call number_to_rank outside of this function)

    user_card_sum = 0
    for card in user_cards["displayed"]:
        user_card_sum += Card.RANK_TO_NUMBER[str(card).split("-")[1]]

    # dealer draws a card if their sum is under 17
    dealer_cards_list = []
    for status in ("hidden", "displayed"):
        dealer_cards_list.append(dealer_cards[status])

    return user_card_sum


def check_who_wins():
    """
    Wriate a short summary of this function

    Write a description of this function in details.

    Args:
        sample_arguments:

    Returns:
        None
    """
    # TODO: Please write a logic

    return None


def dealer_draw_cards(dealer_cards, deck):
    """
    Write a short summary of this function

    Write a description of this function in details.

    Args:
        sample_arguments:

    Returns:
        None
    """
    # TODO: Please write a logic ここからね
    # dealer draws a card if their sum is under 17
    dealer_cards_list = []
    dealer_card_sum = 0
    for status in ("hidden", "displayed"):
        dealer_cards_list.append(dealer_cards[status])

    for card in dealer_cards_list:
        dealer_card_sum += Card.RANK_TO_NUMBER[str(card).split("-")[1]]

    if dealer_card_sum <17:
        card_picked = deck.pick_card(1)
        print(card_picked)
        # dealer_cards["hidden"] = card_picked
        # dealer_cards.update(hidden=card_picked)
        dealer_cards["hidden"].append(card_picked)
    else:
        pass

    return dealer_cards

if __name__ == "__main__":
    start_game()