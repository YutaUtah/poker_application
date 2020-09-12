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
    # Instantiate the Deck object from deck.py
    deck = Deck()
    # Initial setting: both user and dealer draw 2 cards
    user_cards = deck.pick_card(2)
    dealer_cards = deck.pick_card(2)

    # todo: without return value on this function, how does it work?
    # display_cards(user_cards, dealer_cards)

    """
    Examples:
    user_cards = {"displayed":[6, 11], "hidden": []}
    dealer_cards = {"displayed":[8], "hidden": [12]}
    """
    user_cards, dealer_cards = display_cards(user_cards, dealer_cards)
    # User could choose whether or not they pick additional card
    user_cards = user_decide_draw_cards(user_cards, deck)
    # Dealer needs to pick additional card if their remaining sum is under 17
    dealer_cards = dealer_draw_cards(dealer_cards, deck)

    if check_the_sum(user_cards) > 21:
        return 0







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


def check_the_sum(user_cards):
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

    return user_card_sum


def dealer_draw_cards(dealer_cards, deck):
    """
    Write a short summary of this function
    If dealer's 2 cards sum is less than 17, 1 more card will be added to their "hidden" card stack

    Args:
        dealer_cards:
        deck:

    Returns:
        dealer_cards
    """

    dealer_card_sum = 0

    for status in ("hidden", "displayed"):
        for card_idx in range(len(dealer_cards[status])):
            dealer_card_sum += Card.RANK_TO_NUMBER[str(dealer_cards[status][card_idx]).split("-")[1]]

    if dealer_card_sum < 17:
        card_picked = deck.pick_card(1)
        dealer_cards["hidden"].append(card_picked[0])
    else:
        return dealer_cards

    return dealer_cards


def check_who_wins(user_cards, dealer_cards):
    """
    Compare the cards sum of user and dealer, and bigger number will win

    Args:
        user_cards:
        dealer_cards:


    Returns:
        None
    """
    # TODO: Please write a logic

    return None

if __name__ == "__main__":
    start_game()