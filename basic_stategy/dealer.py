# from hand import Hand

# class Dealer:
#     def __init__(self):
#         self.hand = Hand()

#     def play(self, deck, counter=None):  # Accept optional counter
#         while True:
#             value = self.hand.get_value()
#             soft = any(card.face == 'A' for card in self.hand.cards)
#             if value < 17 or (value == 17 and soft):  # dealer hits soft 17 (optional rule)
#                 card = deck.draw()
#                 self.hand.add_card(card)
#                 if counter:
#                     counter.update(card)  # Track dealer card
#             else:
#                 break

#     def get_upcard(self):
#         return self.hand.cards[0]

#     def __str__(self):
#         return f"Dealer: {self.hand} (value: {self.hand.get_value()})"

from hand import Hand

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def play(self, deck):
        while True:
            value = self.hand.get_value()
            soft = any(card.face == 'A' for card in self.hand.cards)
            if value < 17:
                self.hand.add_card(deck.draw())
            else:
                break

    def get_upcard(self):
        return self.hand.cards[0]

    def __str__(self):
        return f"Dealer: {self.hand} (value: {self.hand.get_value()})"