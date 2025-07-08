# from hand import Hand
# from basic_strategy import basic_strategy
# from dealer import Dealer

# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.hands = []
#         self.doubled = []
#         self.surrendered = []

#     def play(self, deck, dealer_upcard,counter=None):
#         self.hands = []
#         self.doubled = []
#         self.surrendered = []

#         initial_hand = Hand()
#         initial_hand.add_card(deck.draw())
#         initial_hand.add_card(deck.draw())

#         self.hands.append(initial_hand)
#         self.doubled.append(False)
#         self.surrendered.append(False)

#         i = 0
#         while i < len(self.hands):
#             hand = self.hands[i]

#             # SPLITTING (multi-hand)
#             if hand.can_split() and len(self.hands) < 4:
#                 face = hand.cards[0].face
#                 decision = basic_strategy(
#                     player_total=hand.get_value(),
#                     dealer_upcard=dealer_upcard.value(),
#                     soft=False,
#                     pair_face=face
#                 )
#                 if decision == 'split':
#                     card1, card2 = hand.cards
#                     new_hand1 = Hand(); new_hand2 = Hand()
#                     new_hand1.add_card(card1); new_hand1.add_card(deck.draw())
#                     new_hand2.add_card(card2); new_hand2.add_card(deck.draw())
#                     self.hands[i] = new_hand1
#                     self.hands.insert(i + 1, new_hand2)
#                     self.doubled[i] = False
#                     self.doubled.insert(i + 1, False)
#                     self.surrendered[i] = False
#                     self.surrendered.insert(i + 1, False)
#                     continue

#             # DECISION LOOP
#             while True:
#                 value = hand.get_value()
#                 soft = any(card.face == 'A' for card in hand.cards)
#                 decision = basic_strategy(value, dealer_upcard.value(), soft)

#                 if decision == 'surrender' and len(hand.cards) == 2:
#                     self.surrendered[i] = True
#                     break
#                 elif decision == 'hit':
#                     hand.add_card(deck.draw())
#                     if hand.is_bust():
#                         break
#                 elif decision == 'double' and len(hand.cards) == 2:
#                     hand.add_card(deck.draw())
#                     self.doubled[i] = True
#                     break
#                 else:
#                     break

#             i += 1
from hand import Hand
from basic_strategy import basic_strategy
from dealer import Dealer

class Player:
    def __init__(self, name):
        self.name = name
        self.hands = []
        self.doubled = []
        self.surrendered = []

    def play(self, deck, dealer_upcard, counter=None):
        self.hands = []
        self.doubled = []
        self.surrendered = []

        # Initial hand
        first_hand = Hand()
        card1 = deck.draw()
        card2 = deck.draw()
        first_hand.add_card(card1)
        first_hand.add_card(card2)

        if counter:
            counter.update(card1)
            counter.update(card2)

        self.hands.append(first_hand)
        self.doubled.append(False)
        self.surrendered.append(False)

        # Handle splitting (if allowed by basic strategy)
        if first_hand.can_split():
            face = first_hand.cards[0].face
            decision = basic_strategy(
                player_total=first_hand.get_value(),
                dealer_upcard=dealer_upcard.value(),
                soft=False,
                pair_face=face
            )
            if decision == 'split':
                h1 = Hand()
                h2 = Hand()
                h1.add_card(first_hand.cards[0])
                h2.add_card(first_hand.cards[1])
                new_card1 = deck.draw()
                new_card2 = deck.draw()
                h1.add_card(new_card1)
                h2.add_card(new_card2)

                if counter:
                    counter.update(new_card1)
                    counter.update(new_card2)

                self.hands = [h1, h2]
                self.doubled = [False, False]
                self.surrendered = [False, False]

        # Play each hand
        for i, hand in enumerate(self.hands):
            while True:
                value = hand.get_value()
                soft = any(card.face == 'A' for card in hand.cards)
                decision = basic_strategy(value, dealer_upcard.value(), soft)

                if decision == 'surrender' and len(hand.cards) == 2:
                    self.surrendered[i] = True
                    break
                elif decision == 'hit':
                    card = deck.draw()
                    hand.add_card(card)
                    if counter: counter.update(card)
                    if hand.is_bust():
                        break
                elif decision == 'double' and len(hand.cards) == 2:
                    card = deck.draw()
                    hand.add_card(card)
                    self.doubled[i] = True
                    if counter: counter.update(card)
                    break
                else:
                    break
