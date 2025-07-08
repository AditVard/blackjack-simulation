import matplotlib.pyplot as plt
from simulate import simulate
import numpy as np
if __name__ == "__main__":
    stats = simulate(n_rounds=100000)

    print("Simulation Results:")
    print("Wins     :", stats["wins"])
    print("Losses   :", stats["losses"])
    print("Pushes   :", stats["pushes"])

    total_games = stats["wins"] + stats["losses"] + stats["pushes"]
    print(f"\nWin %    : {100 * stats['wins'] / total_games:.2f}%")
    print(f"Loss %   : {100 * stats['losses'] / total_games:.2f}%")
    print(f"Push %   : {100 * stats['pushes'] / total_games:.2f}%")
    print(f"\nNet Return: {stats['net_return']:.2f} units")
    print(f"EV per game: {stats['net_return'] / total_games:.4f} units")
    std_dev = np.std(stats["bankroll_history"])
    print(f"Std Dev of Bankroll: {std_dev:.2f} units")
    # Plotting
    games = list(range(len(stats["bankroll_history"])))
    plt.figure(figsize=(10, 6))
    plt.plot(games, stats["bankroll_history"], label="Bankroll", color='blue')
    plt.plot(games, stats["ev_history"], label="EV per game", color='orange')
    plt.xlabel("Number of Games")
    plt.ylabel("Bankroll / EV")
    plt.title("Blackjack Strategy Performance")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

