# betting.py

class FlatBetting:
    def __init__(self, unit=1):
        self.unit = unit  

    def bet_amount(self, bankroll, last_outcome=None):
        return self.unit


class Martingale:
    def __init__(self, base_unit=1):
        self.base_unit = base_unit
        self.loss_streak = 0

    def bet_amount(self, bankroll, last_outcome=None):
        if last_outcome == "lose":
            self.loss_streak += 1
        else:
            self.loss_streak = 0
        return min(bankroll, self.base_unit * (2 ** self.loss_streak))


class KellyCriterion:
    def __init__(self, edge=0.005, win_prob=0.42):  # FIXED: typo in __init__
        self.edge = edge
        self.win_prob = win_prob

    def bet_amount(self, bankroll, last_outcome=None):
        b = 1  # payout on a win
        f = (self.win_prob * (b + 1) - 1) / b
        f = max(0, min(f, 1))  # keep f in [0, 1]
        return max(1, int(bankroll * f))  # at least 1 unit


class CustomBetting:
    def __init__(self):
        self.counter = 0

    def bet_amount(self, bankroll, last_outcome=None):
        if last_outcome == "lose":
            self.counter += 1
        else:
            self.counter = 0
        return min(bankroll, 1 + self.counter)
class ModifiedMartingale:
    def __init__(self, base_unit=1):
        self.base_unit = base_unit
        self.loss_streak = 0
        self.total_locked_profit = 0

    def bet_amount(self, bankroll, last_outcome):
        if last_outcome == "lose":
            self.loss_streak += 1
        else:
            self.loss_streak = 0
            self.total_locked_profit += self.base_unit

        bet = self.base_unit * (2 ** self.loss_streak)

        return min(bet, bankroll) 