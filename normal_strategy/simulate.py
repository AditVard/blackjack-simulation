from game import setup_game, player_turn, dealer_turn, determine_winner

def simulate(n_games=10000, initial_bankroll=1000, bet_strategy=None):
    stats = {
        "player_wins": 0,
        "dealer_wins": 0,
        "pushes": 0,
        "net_return": 0,
        "bankroll_history": [initial_bankroll],
        "ev_history": [],
        "bet_history": []
    }

    bankroll = initial_bankroll
    last_result = None

    for i in range(n_games):
        if bankroll <= 0:
            break

        bet = bet_strategy.bet_amount(bankroll, last_result) if bet_strategy else 10
        bet = min(bet, bankroll)
        stats["bet_history"].append(bet)
        bankroll -= bet

        deck, player, dealer = setup_game()

        player_blackjack = player.hand.is_blackjack()
        dealer_blackjack = dealer.hand.is_blackjack()

        if player_blackjack and not dealer_blackjack:
            bankroll += bet * 2.5
            stats["player_wins"] += 1
            last_result = "win"
        elif dealer_blackjack and not player_blackjack:
            stats["dealer_wins"] += 1
            last_result = "lose"
        elif player_blackjack and dealer_blackjack:
            bankroll += bet
            stats["pushes"] += 1
            last_result = "push"
        else:
            player_turn(player, dealer, deck)

            if player.hand.is_bust():
                stats["dealer_wins"] += 1
                last_result = "lose"
            else:
                dealer_turn(dealer, deck)
                result = determine_winner(player, dealer)

                if result == "Player wins":
                    bankroll += bet * 2
                    stats["player_wins"] += 1
                    last_result = "win"
                elif result == "Dealer wins":
                    stats["dealer_wins"] += 1
                    last_result = "lose"
                else:
                    bankroll += bet
                    stats["pushes"] += 1
                    last_result = "push"

        stats["net_return"] = bankroll - initial_bankroll
        stats["bankroll_history"].append(bankroll)
        stats["ev_history"].append(stats["net_return"] / (i + 1))

    stats["expected_value_per_game"] = stats["net_return"] / max(1, len(stats["ev_history"]))
    stats["final_bankroll"] = bankroll
    return stats