from deck import Deck
from dealer import Dealer
from player import Player

def setup_game():
    deck = Deck()
    dealer = Dealer()
    player = Player(name="You", strategy="random")  # or use "basic" if needed
    for _ in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
    return deck, player, dealer

def player_turn(player, dealer, deck):
    dealer_upcard = dealer.hand.cards[0]  # simply reveal first card
    player.play(deck, dealer_upcard)

def dealer_turn(dealer, deck):
    dealer.play(deck)

def determine_winner(player, dealer):
    if player.hand.is_bust():
        return "Dealer wins"
    elif dealer.hand.is_bust():
        return "Player wins"
    else:
        player_value = player.hand.get_value()
        dealer_value = dealer.hand.get_value()
        if player_value > dealer_value:
            return "Player wins"
        elif dealer_value > player_value:
            return "Dealer wins"
        else:
            return "Push"

def run_game():
    deck, player, dealer = setup_game()

    print("🎲 Welcome to Blackjack!")
    print(f"Dealer's upcard: {dealer.hand.cards[0]}")  # Show first card only
    print(f"Your hand: {player.hand} (value: {player.hand.get_value()})")

    player_turn(player, dealer, deck)

    if not player.hand.is_bust():
        dealer_turn(dealer, deck)

    print("\n--- Final Hands ---")
    print(f"Your hand: {player.hand} (value: {player.hand.get_value()})")
    print(f"Dealer's hand: {dealer.hand} (value: {dealer.hand.get_value()})")

    result = determine_winner(player, dealer)
    print(" Result:", result)
