from .deck import Deck
from .player import Player

class GameManager:
    def __init__(self, num_players):
        if not (2 <= num_players <= 4):
            raise ValueError("Number of players must be between 2 and 4.")
        
        self.deck = Deck()
        self.players = [Player(player_id=i) for i in range(num_players)]
        self.discard_pile = [self.deck.draw_card()]
        self.current_player = 0

        # Deal 5 cards to each player
        for _ in range(5):
            for player in self.players:
                player.add_card(self.deck.draw_card())

    def is_valid_play(self, card):
        top_card = self.discard_pile[-1]
        return card.color == top_card.color or card.value == top_card.value

    def play_card(self, card):
        self.players[self.current_player].remove_card(card)
        self.discard_pile.append(card)

    def draw_card(self):
        new_card = self.deck.draw_card()
        self.players[self.current_player].add_card(new_card)

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def check_winner(self):
        for i, player in enumerate(self.players):
            if not player.hand:
                return i
        return None
