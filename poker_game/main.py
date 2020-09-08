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

    :return: None
    """
    deck = Deck()

    user_cards, dealer_cards = draw_two_cards_from_deck(deck)

    # Examples:
    user_cards = {"displayed":[6, 11], "hidden": []}
    dealer_cards = {"displayed":[8], "hidden": [12]}

    display_cards(user_cards, dealer_cards)

    user_cards = user_decide_draw_cards(user_cards, deck)

    if check_the_sum(user_cards) > 21:
        return 0

    dealer_cards = deader_draw_cards(dealer_cards, deck)

    if check_the_sum(dealer_cards) > 21:
        return 1

    results = check_who_wins(user_cards, dealer_cards)

    return results
