import random
from .card import Card

class Deck:
    COLORS = ["Red", "Yellow", "Green", "Blue"]
    VALUES = list(range(1, 10))

    def __init__(self):
        self.cards = [Card(color, value) for color in self.COLORS for value in self.VALUES]
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            raise ValueError("No more cards in the deck.")
        return self.cards.pop()
