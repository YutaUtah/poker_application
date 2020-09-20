from poker_game.deck import Deck
from poker_game.card import Card


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
    once the dealer stops drawing a card without the number going above 21,
    will check whether user or dealer has a closer number of sum to 21.

    Returns:
        None
    """
    # Instantiate the Deck object from deck.py
    deck = Deck()
    # Initial setting: both user and dealer draw 2 cards

    user_cards = {"displayed": [], "hidden": []}
    dealer_cards = {"displayed": [], "hidden": []}

    user_cards["displayed"] = deck.pick_card(2)
    dealer_cards["displayed"] = deck.pick_card(1)
    dealer_cards["hidden"] = deck.pick_card(1)

    # todo: without return value on this function, how does it work?
    # display_cards(user_cards, dealer_cards)


    # Examples:
    # user_cards = {"displayed":[6, 11], "hidden": []}
    # dealer_cards = {"displayed":[8], "hidden": [12]}

    display_cards(user_cards, dealer_cards)
    user_cards = user_decide_draw_cards(user_cards, deck)
    if check_the_sum(user_cards) > 21:
        comment = "Dealer wins"
        output_result(user_cards, dealer_cards, comment)
        return None
    # Dealer needs to pick additional card if their remaining sum is under 17
    dealer_cards = dealer_draw_cards(dealer_cards, deck)
    check_who_wins(user_cards, dealer_cards)

    return None

def display_cards(user_cards, dealer_cards):
    """
    Draw two cards for users and dealers from deck object.

    Create two empty dictionarys with a key displayed and hidden,
    call a function draw_a_card() from Deck objects,
    assign two cards to displayed in user_cards,
    assign one card to displayed and one card to hidden in dealer_cards,
    return these dictionaries.


    Args:
        user_cards:
        dealer_cards:

    Returns:
        user_cards, dealer_cards
    """

    print("Your cards:")
    for card in user_cards["displayed"]:
        print(card)
    print(user_cards["displayed"], sep=' ')
    print("Dealer's displayed card: ")
    for card in dealer_cards["displayed"]:
        print(str(card))
    return None


def user_decide_draw_cards(game_card_user, deck):
    """
    Shows user's cards first, ask if they want to draw 1 more card
    Keep doing this until they choose not to draw
    If user's cards sum is over 21, quit the application and the user will lose

    Args:
        game_card_user:
        deck:

    Returns:
        game_card_user
    """

    decided = True
    while decided:
        draw_or_not = input("You have 2 cards {}. Do you want to draw 1 more card? [y/n] \n"
                            .format(', '.join(str(x) for x in game_card_user["displayed"])))

        if draw_or_not.lower() == 'y':
            user_next_card = deck.pick_card(1)
            print(user_next_card)
            game_card_user["displayed"].append(user_next_card[0])
            print("your current cards are {}".format(', '.join(str(x) for x in game_card_user["displayed"])))
            if check_the_sum(game_card_user) > 21:
                print("Your cards is over 21, You lose!")
                break
            pass
        elif draw_or_not.lower() == 'n':
            break
        else:
            print("Please input appropriate answer!")

    return game_card_user


def check_the_sum(player_cards):
    """
    Check the sum of given player's cards

    Args:
        player_cards:

    Returns:
        cards_sum
    """
    # TODO: Please write a logic (what happens if i call number_to_rank outside of this function)

    cards_sum = 0

    """
    for status_cards in player_cards.items: 
    for each_card in status_cards: 
    cards_sum += Card.RANK_TO_NUMBER[each_card.split("-")[1]] 
    
    for status in ("hidden", "displayed"): 
    for card_idx in range(len(player_cards[status])): 
    cards_sum += Card.RANK_TO_NUMBER[str(player_cards[status][card_idx]).split("-")[1]]
    """

    for status in ("hidden", "displayed"):
        for card_idx in range(len(player_cards[status])):
            cards_sum += Card.RANK_TO_NUMBER[str(player_cards[status][card_idx]).split("-")[1]]

    return cards_sum


def dealer_draw_cards(dealer_cards, deck):
    """
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
            dealer_card_sum += Card.RANK_TO_NUMBER[dealer_cards[status][card_idx].split("-")[1]]

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
    if check_the_sum(dealer_cards) > 21:
        print("You win {}!".format(', '.join(str(x) for x in user_cards["displayed"])))
        comment = "You win"
        output_result(user_cards, dealer_cards, comment)
    elif check_the_sum(user_cards) > check_the_sum(dealer_cards):
        print("You win {}!".format(', '.join(str(x) for x in user_cards["displayed"])))
        comment = "You win"
        output_result(user_cards, dealer_cards, comment)
    elif check_the_sum(user_cards) < check_the_sum(dealer_cards):
        print("Dealer wins {}!".format(', '.join(str(x) for status in ("hidden", "displayed")
                                                 for x in dealer_cards[status])))
        comment = "Dealer wins"
        output_result(user_cards, dealer_cards, comment)
    elif check_the_sum(user_cards) == check_the_sum(dealer_cards):
        print("You guys tied! Yours: {} Theirs: {}".format(', '.join(str(x) for x in user_cards["displayed"]),
                                            ', '.join(str(x) for status in ("hidden", "displayed")
                                                      for x in dealer_cards[status])))
        comment = "Tied"
        output_result(user_cards, dealer_cards, comment)


    return None

def output_result(user_cards, dealer_cards, comment):
    """
    Output the result in result.csv.
    If no csv file is indicated, create one

    Args:
        user_cards:
        dealer_cards:
        comment:

    Returns:
        None
    """
    path = './result.csv'
    user_sum = check_the_sum(user_cards)
    dealer_sum = check_the_sum(dealer_cards)

    with open(path, mode="a+") as f:
        f.write(str(user_sum) + " " + str(dealer_sum) + " " + comment + "\n")

if __name__ == "__main__":
    game_counter = 1
    print("\n***********************************  Game {}  ***********************************\n".format(game_counter))
    while True:
        start_game()
        user_decision = input("\nDo you want to continue? [y/n]\n")
        if user_decision.lower() == 'n':
            print("\nThank you for playing our BlackJack!!")
            break
        game_counter += 1
        print("\n***********************************  Game {}  ***********************************\n".format(game_counter))