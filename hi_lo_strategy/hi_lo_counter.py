# hi_lo_counter.py

class HiLoCounter:
    def __init__(self):
        self.running_count = 0

    def update(self, card):
        if card.face in ['2', '3', '4', '5', '6']:
            self.running_count += 1
        elif card.face in ['10', 'J', 'Q', 'K', 'A']:
            self.running_count -= 1
        # 7, 8, 9 = 0 → do nothing

    def reset(self):
        self.running_count = 0

    def get_true_count(self, decks_remaining):
        if decks_remaining == 0:
            return 0
        return self.running_count / decks_remaining
