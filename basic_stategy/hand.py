class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def reset(self):
        self.cards = []

    def get_value(self):
        value = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.face == 'A')
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    def is_bust(self):
        return self.get_value() > 21

    def __str__(self):
        return ', '.join(str(c) for c in self.cards)
    def can_split(self):
        return len(self.cards) == 2 and self.cards[0].face == self.cards[1].face
