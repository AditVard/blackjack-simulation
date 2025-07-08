class Game():
    deck = Deck()
    players = []
    num_players = int(input("Number of players:"))
    for i in range(num_players):
        name = input(f"Player {i+1} name:")
        players.append(Player(name))