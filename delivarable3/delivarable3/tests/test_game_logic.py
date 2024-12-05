# import pytest
# from backend.game_logic.card import PlayingCard
# from backend.game_logic.player import GamePlayer
# from backend.game_logic.deck import CardDeck
# from backend.game_logic.game_manager import GameMaster

# def test_card_creation():
#     card = PlayingCard("Red", "5")
#     assert card.color == "Red"
#     assert card.value == "5"

# def test_player_add_card():
#     player = GamePlayer("TestPlayer")
#     card = PlayingCard("Blue", "8")
#     player.receive_card(card)
#     assert len(player.get_hand()) == 1

# def test_deck_shuffle():
#     deck = CardDeck()
#     deck.shuffle_deck()
#     assert len(deck.cards) == 108  # Assuming a full Uno deck

# def test_game_manager_init():
#     manager = GameMaster(2)
#     assert len(manager.players) == 2
#     assert len(manager.deck.cards) > 0
