from hand import Hand

class Player:
    def __init__(self, name="Player", strategy="random"):
        self.name = name
        self.hand = Hand()
        self.strategy = strategy

    def add_card(self, card):
        self.hand.add_card(card)

    def reset(self):
        self.hand.reset()

    def make_decision(self, dealer_upcard):
        value = self.hand.get_value()

        # Very basic rules (for use with betting strategy simulations)
        if value <= 11:
            return "hit"
        elif 12 <= value <= 16 and dealer_upcard.value() >= 7:
            return "hit"
        elif value >= 17:
            return "stand"
        else:
            return "stand"

    def play(self, deck, dealer_upcard):
        while True:
            if self.hand.is_bust():
                break

            decision = self.make_decision(dealer_upcard)

            if decision == "hit":
                self.add_card(deck.deal())
            elif decision == "stand":
                break
