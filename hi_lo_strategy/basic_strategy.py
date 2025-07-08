def basic_strategy(player_total, dealer_upcard, soft, pair_face=None):
        """
        Returns: 'hit', 'stand', 'double', 'split', or 'surrender'
        """
        if pair_face:  # Pair Splitting logic
            pair = pair_face
            if pair == 'A' or pair == '8':
                return 'split'
            if pair == 'T':
                return 'stand'
            if pair == '9':
                return 'split' if dealer_upcard in [2, 3, 4, 5, 6, 8, 9] else 'stand'
            if pair == '7':
                return 'split' if dealer_upcard <= 7 else 'hit'
            if pair == '6':
                return 'split' if dealer_upcard <= 6 else 'hit'
            if pair == '5':
                return 'double' if dealer_upcard in range(2, 10) else 'hit'
            if pair == '4':
                return 'split' if dealer_upcard in [5, 6] else 'hit'
            if pair == '3' or pair == '2':
                return 'split' if dealer_upcard <= 7 else 'hit'

        if soft:
            if player_total == 20: return 'stand'
            if player_total == 19: return 'stand' if dealer_upcard in [2, 3, 4, 5, 6, 7, 8] else 'stand'
            if player_total == 18:
                if dealer_upcard in [3, 4, 5, 6]: return 'double'
                elif dealer_upcard in [2, 7, 8]: return 'stand'
                else: return 'hit'
            if player_total == 17: return 'double' if dealer_upcard in [3, 4, 5, 6] else 'hit'
            if player_total == 16 or player_total == 15: return 'double' if dealer_upcard in [4, 5, 6] else 'hit'
            if player_total == 14 or player_total == 13: return 'double' if dealer_upcard in [5, 6] else 'hit'

        else:
            if player_total >= 17: return 'stand'
            if player_total == 16 and dealer_upcard in [9, 10, 1]: return 'surrender'
            if player_total == 15 and dealer_upcard == 1: return 'surrender'
            if player_total == 16: return 'stand' if dealer_upcard in [2, 3, 4, 5, 6] else 'hit'
            if player_total == 15: return 'stand' if dealer_upcard in [2, 3, 4, 5, 6] else 'hit'
            if player_total == 14: return 'stand' if dealer_upcard in [2, 3, 4, 5, 6] else 'hit'
            if player_total == 13: return 'stand' if dealer_upcard in [2, 3, 4, 5, 6] else 'hit'
            if player_total == 12: return 'stand' if dealer_upcard in [4, 5, 6] else 'hit'
            if player_total == 11: return 'double'
            if player_total == 10: return 'double' if dealer_upcard <= 9 else 'hit'
            if player_total == 9: return 'double' if dealer_upcard in [3, 4, 5, 6] else 'hit'
            return 'hit'
