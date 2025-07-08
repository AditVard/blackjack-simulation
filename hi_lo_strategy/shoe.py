import random
from card import Card

class Shoe:
    def __init__(self, n_decks=6):
        self.n_decks = n_decks
        self.cards = [Card(s, f) for s in Card.SUITS for f in Card.FACES] * n_decks
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def penetration_reached(self):
        return len(self.cards) < 0.25 * 52 * self.n_decks
