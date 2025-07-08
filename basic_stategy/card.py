class Card:
    SUITS = ['♠', '♥', '♦', '♣']
    FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def value(self):
        return self.VALUES[self.face]

    def __str__(self):
        return f"{self.face}{self.suit}"
