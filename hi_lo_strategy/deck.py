import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(suit, face) for suit in Card.SUITS for face in Card.FACES]
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            self.__init__()
        return self.cards.pop()
