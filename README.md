# ♠️ Blackjack Strategy Simulation

A Python-based simulation project to evaluate different Blackjack strategies using Monte Carlo methods. It compares naïve strategies, betting systems, and optimal strategies like Basic Strategy and Hi-Lo Card Counting.

📄 **Full Report:** [Blackjack Simulation Summary.pdf](./Blackjack%20Simulation%20Summary.pdf)

---

## 🎯 Strategies Covered

- Naïve Strategies  
  - Random Play  
  - Hit if < 17  
  - Basic Heuristic Rules  

- Betting Systems  
  - Flat Betting  
  - Martingale  
  - Modified Martingale  
  - Kelly Criterion  
  - Custom Loss-Based Betting  

- Optimal Strategies  
  - Basic Strategy (Decision Chart)  
  - Hi-Lo Card Counting (Running Count)

---

## 📁 Project Structure

blackjack-simulation/
├── Blackjack Simulation Summary.pdf     # Full report with EV, bankroll, graphs  
├── basic_strategy/                      # Basic play logic and simulator  
├── hi_lo_strategy/                      # Card counting strategy simulation  
└── normal_strategy/                     # Betting system simulations  

---

## 🚀 How to Run

# Run Basic Strategy Simulation
cd basic_strategy  
python main.py  

# Run Hi-Lo Card Counting Simulation
cd ../hi_lo_strategy  
python main2.py  

# Run Betting System Simulation
cd ../normal_strategy  
python main_sim.py  

