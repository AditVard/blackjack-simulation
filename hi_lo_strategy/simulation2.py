from shoe import Shoe
from dealer import Dealer
from player import Player
from hi_lo_counter import HiLoCounter

def simulate(n_rounds=10000, base_bet=1):
    stats = {
        "wins": 0, "losses": 0, "pushes": 0,
        "net_return": 0.0,
        "bankroll_history": [],
        "ev_history": [],
        "true_count_history": []
    }

    bankroll = 0.0
    cumulative_ev = 0.0

    deck = Shoe()
    counter = HiLoCounter()

    for game in range(n_rounds):
        if deck.penetration_reached():
            deck = Shoe()
            counter.reset()

        dealer = Dealer()
        player = Player("P1")

        # Deal dealer's cards and count them
        card1 = deck.draw(); counter.update(card1); dealer.hand.add_card(card1)
        card2 = deck.draw(); counter.update(card2); dealer.hand.add_card(card2)

        # Player logic (draws and counts inside Player.play)
        player.play(deck, dealer.get_upcard(), counter)

        # Dealer logic (draws and counts inside Dealer.play)
        dealer.play(deck, counter)

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

            # Track result
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

        # Save true count snapshot
        decks_remaining = len(deck.cards) / 52
        true_count = counter.get_true_count(decks_remaining)
        stats["true_count_history"].append(true_count)

    stats["net_return"] = bankroll
    return stats
