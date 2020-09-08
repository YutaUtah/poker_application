from poker_game.deck import Deck

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

    user_cards, dealer_cards = draw_two_cards_from_deck(deck)

    # Examples:
    # user_cards = {"displayed":[6, 11], "hidden": []}
    # dealer_cards = {"displayed":[8], "hidden": [12]}

    display_cards(user_cards, dealer_cards)

    user_cards = user_decide_draw_cards(user_cards, deck)

    if check_the_sum(user_cards) > 21:
        return 0

    dealer_cards = deader_draw_cards(dealer_cards, deck)

    if check_the_sum(dealer_cards) > 21:
        return 1

    results = check_who_wins(user_cards, dealer_cards)

    return results


def draw_two_cards_from_deck(deck):
    """
    Draw two cards for users and dealers from deck object.

    Write a description of this function in details.

    Args:
        deck: a card deck object

    Returns:
        two dictionaries with keys displayed and hidden
    """
    #TODO: Please write a logic
    user_cards = {"displayed":[], "hidden": []}
    dealer_cards = {"displayed": [], "hidden": []}

    user_cards["displayed"].append(deck.draw_a_card())
    dealer_cards["displayed"].append(deck.draw_a_card())
    user_cards["displayed"].append(deck.draw_a_card())
    dealer_cards["hidden"].append(deck.draw_a_card())

    return user_cards, dealer_cards


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

    return None


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
