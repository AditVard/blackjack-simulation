import matplotlib.pyplot as plt
from simulation2 import simulate  # Make sure the filename is correct

if __name__ == "__main__":
    stats = simulate(n_rounds=100000, base_bet=1)

    # Basic stats
    print("Simulation Results:")
    print("Wins     :", stats["wins"])
    print("Losses   :", stats["losses"])
    print("Pushes   :", stats["pushes"])

    total_games = stats["wins"] + stats["losses"] + stats["pushes"]
    win_pct = 100 * stats["wins"] / total_games
    loss_pct = 100 * stats["losses"] / total_games
    push_pct = 100 * stats["pushes"] / total_games

    print(f"\nWin %    : {win_pct:.2f}%")
    print(f"Loss %   : {loss_pct:.2f}%")
    print(f"Push %   : {push_pct:.2f}%")

    print(f"\nNet Return: {stats['net_return']:.2f} units")
    print(f"EV per game: {stats['net_return'] / total_games:.4f} units")

    # Optional: Show ROI per 100 hands
    roi = 100 * stats["net_return"] / total_games
    print(f"ROI per 100 hands: {roi:.2f} units")

    # Plot bankroll + EV
    games = list(range(len(stats["bankroll_history"])))

    plt.figure(figsize=(12, 6))
    plt.plot(games, stats["bankroll_history"], label="Bankroll", color='blue')
    plt.plot(games, stats["ev_history"], label="EV per game", color='orange')
    plt.xlabel("Number of Hands")
    plt.ylabel("Bankroll / EV")
    plt.title("Blackjack with Hi-Lo Card Counting")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Optional: Plot True Count Over Time
    plt.figure(figsize=(12, 4))
    plt.plot(stats["true_count_history"], label="True Count", color='green', alpha=0.6)
    plt.axhline(0, color='gray', linestyle='--')
    plt.xlabel("Number of Hands")
    plt.ylabel("True Count")
    plt.title("True Count Progression")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
