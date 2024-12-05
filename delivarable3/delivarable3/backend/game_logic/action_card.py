from game_logic.card import PlayingCard

class SpecialCard(PlayingCard):
    def __init__(self, color, action):
        super().__init__(color, action)
        self.action = action

    def execute_action(self, game_manager):
        if self.action == "Skip":
            game_manager.skip_next_player()
        elif self.action == "Reverse":
            game_manager.reverse_play_order()
        elif self.action == "Draw Two":
            game_manager.force_draw_two()
