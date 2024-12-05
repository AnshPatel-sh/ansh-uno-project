from flask import Flask, jsonify, request
from game_logic.game_manager import GameManager

app = Flask(__name__)
game_manager = GameManager(num_players=2)

@app.route('/start', methods=['POST'])
def start_game():
    game_manager.start_game()
    return jsonify({"message": "Game started!"})

@app.route('/play_turn', methods=['POST'])
def play_turn():
    game_manager.play_turn()
    return jsonify({"message": "Turn played."})

if __name__ == "__main__":
    app.run(debug=True)
