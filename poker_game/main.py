#todo:
# このimportこの書き方でいいかな
from deck import Deck


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
    a, b = display_cards(user_cards, dealer_cards)
    # todo: without return value on this function, how does it work?
    # display_cards(user_cards, dealer_cards)


    user_cards = user_decide_draw_cards(user_cards, deck)

    if check_the_sum(user_cards) > 21:
        return 0

    dealer_cards = deader_draw_cards(dealer_cards, deck)

    if check_the_sum(dealer_cards) > 21:
        return 1

    results = check_who_wins(user_cards, dealer_cards)

    return results


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
    game_card_dealer["displayed"], game_card_dealer["hidden"] = dealer_cards[0], dealer_cards[1]

    return game_card_user, game_card_dealer


def user_decide_draw_cards():
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


def check_the_sum():
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


def deader_draw_cards():
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

