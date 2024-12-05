class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)
