from betting import FlatBetting, Martingale, KellyCriterion, CustomBetting, ModifiedMartingale
from simulate import simulate
import matplotlib.pyplot as plt

# Choose strategy
strategy = ModifiedMartingale(base_unit=1)  # Example: Flat Betting with unit 1

# Run simulation
stats = simulate(n_games=10000, initial_bankroll=1000, bet_strategy=strategy)

# Print Results
print(f"Strategy: {strategy.__class__.__name__}")
print(f"Player wins : {stats['player_wins']} ({stats['player_wins'] / sum([stats['player_wins'], stats['dealer_wins'], stats['pushes']])*100:.2f}%)")
print(f"Dealer wins : {stats['dealer_wins']} ({stats['dealer_wins'] / sum([stats['player_wins'], stats['dealer_wins'], stats['pushes']])*100:.2f}%)")
print(f"Pushes      : {stats['pushes']} ({stats['pushes'] / sum([stats['player_wins'], stats['dealer_wins'], stats['pushes']])*100:.2f}%)")
print(f"\nNet return  : {stats['net_return']} units")
print(f"EV per game : {stats['expected_value_per_game']:.4f} units")
print(f"Final bankroll: {stats['final_bankroll']}")

# Plot results
plt.plot(stats["bankroll_history"], label="Bankroll")
plt.plot(stats["ev_history"], label="EV per game")
plt.xlabel("Number of Games")
plt.ylabel("Bankroll / EV")
plt.legend()
plt.title(f"{strategy.__class__.__name__} Strategy Performance")
plt.grid()
plt.show()
