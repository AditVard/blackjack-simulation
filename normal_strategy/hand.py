from card import Card

class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self,card):
        self.cards.append(card)
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
    def is_bust(self):
        return self.get_value() > 21
    def get_value(self):
        total = 0 
        aces = 0  #  We use this to adjst for our aces like if we ever need to convert 11 to 1 or 1 to 11
        for card in self.cards:
            val = card.value()
            total +=val
            if card.rank == 'A':
                aces+=1
        #Aces converion 
        while total>21 and aces>0:
            total -=10
            aces-=1
        return total 
    def is_soft(self):
        """Return True if the hand is soft (i.e., contains an Ace counted as 11)"""
        total = 0
        ace_count = 0
        for card in self.cards:
            val = card.value()
            total += val
            if card.rank == 'A':
                ace_count += 1

        # If we have an Ace and total <= 21, it's a soft hand
        return ace_count > 0 and total <= 21
    
    def num_cards(self):
        return len(self.cards)
    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21
