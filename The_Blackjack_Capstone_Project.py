import random


def deal_card():
    """Returns a random card value from a standard deck."""
    # 11 represents an Ace. 10s represent 10, Jack, Queen, King.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards_list):
    """Calculates the score of a hand, adjusting for Aces."""
    # 0 represents a Blackjack
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0

    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)

    return sum(cards_list)


def determine_winner(player_score, dealer_score):
    """Compares scores and returns the result."""
    if player_score == dealer_score:
        return "It's a draw!"
    elif dealer_score == 0:
        return "Dealer has a Blackjack. You lose."
    elif player_score == 0:
        return "You have a Blackjack! You win!"
    elif player_score > 21:
        return "You went bust. You lose."
    elif dealer_score > 21:
        return "Dealer went bust. You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose."


def play_blackjack():
    print("\n--- Welcome to Python Blackjack ---")

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_active = True

    while game_active:
        p_score = calculate_score(player_hand)
        d_score = calculate_score(dealer_hand)

        print(f"Your cards: {player_hand}, current score: {p_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if p_score == 0 or d_score == 0 or p_score > 21:
            game_active = False
        else:
            move = input("Type 'y' to hit, or 'n' to stand: ").lower()
            if move == 'y':
                player_hand.append(deal_card())
            else:
                game_active = False

    # Dealer logic: Dealer must hit until their score is 17 or higher
    while d_score != 0 and d_score < 17:
        dealer_hand.append(deal_card())
        d_score = calculate_score(dealer_hand)

    print(f"\nYour final hand: {player_hand}, final score: {p_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {d_score}")
    print(determine_winner(p_score, d_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_blackjack()