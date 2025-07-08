from shoe import Shoe
from dealer import Dealer
from player import Player

def simulate(n_rounds=10000, base_bet=1):
    stats = {
        "wins": 0, "losses": 0, "pushes": 0,
        "net_return": 0.0,
        "bankroll_history": [],
        "ev_history": []
    }

    bankroll = 0.0
    cumulative_ev = 0.0

    deck = Shoe()

    for game in range(n_rounds):
        if deck.penetration_reached():
            deck = Shoe()

        dealer = Dealer()
        player = Player("P1")

        dealer.hand.add_card(deck.draw())
        dealer.hand.add_card(deck.draw())

        player.play(deck, dealer.get_upcard())
        dealer.play(deck)

        for i, hand in enumerate(player.hands):
            bet = base_bet * (2 if player.doubled[i] else 1)
            payout = 0.0

            if player.surrendered[i]:
                payout = -0.5 * base_bet
                result = 'loss'
            elif hand.is_blackjack() and not dealer.hand.is_blackjack():
                payout = 1.5 * base_bet
                result = 'win'
            elif dealer.hand.is_blackjack() and not hand.is_blackjack():
                payout = -base_bet
                result = 'loss'
            elif hand.is_bust():
                payout = -bet
                result = 'loss'
            else:
                player_val = hand.get_value()
                dealer_val = dealer.hand.get_value()

                if dealer.hand.is_bust() or player_val > dealer_val:
                    payout = bet
                    result = 'win'
                elif player_val < dealer_val:
                    payout = -bet
                    result = 'loss'
                else:
                    payout = 0
                    result = 'push'

            if result == 'win':
                stats["wins"] += 1
            elif result == 'loss':
                stats["losses"] += 1
            elif result == 'push':
                stats["pushes"] += 1

            bankroll += payout
            stats["bankroll_history"].append(bankroll)

            ev = (
                1.5 if result == 'win' and hand.is_blackjack() else
                1 if result == 'win' else
                -1 if result == 'loss' else
                0
            )

            if player.doubled[i]:
                ev *= 2
            if player.surrendered[i]:
                ev = -0.5

            cumulative_ev += ev
            stats["ev_history"].append(cumulative_ev * base_bet / len(stats["bankroll_history"]))

    stats["net_return"] = bankroll
    return stats