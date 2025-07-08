from hand import Hand
class Dealer:
    def __init__(self):
        self.hand = Hand()
    def play(self,deck):
        #Dealer will hit until 17 aafter which he will stand soft if on 17
        while True:
            value = self.hand.get_value()

            #When soft we count no of aces
            has_soft_17 = value == 17 and any(card.rank=='A' for card in self.hand.cards)
            if value <17:
                self.hand.add_card(deck.deal())
            else:
                break
    def reset(self):
        self.hand.reset()
    def add_card(self,card):
        self.hand.add_card(card)
    def show_first_card(self):
        #Shows the face up card for player to take a call
        if self.hand.cards:
            return str(self.hand.cards[0])
        return "No card"
    def __str__(self):
        return f"Dealer:{self.hand}(value:{self.hand.get_value()})"
    def get_upcard(self):
        if self.hand.cards:
            return self.hand.cards[0]
        return None
