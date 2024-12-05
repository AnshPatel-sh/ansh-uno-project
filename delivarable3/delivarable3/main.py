from flask import Flask, render_template, request, redirect, url_for
from backend.game_logic.game_manager import GameManager

app = Flask(__name__)

# Global variables
game_manager = None

@app.route("/", methods=["GET", "POST"])
def index():
    global game_manager
    if request.method == "POST":
        num_players = int(request.form["num_players"])
        if num_players < 2 or num_players > 4:
            return render_template("index.html", error="Invalid number of players. Please choose between 2 and 4.")
        game_manager = GameManager(num_players)
        return redirect(url_for("game"))
    return render_template("index.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    global game_manager
    if not game_manager:
        return redirect(url_for("index"))

    current_player = game_manager.current_player
    player_hand = game_manager.players[current_player].hand
    top_card = game_manager.discard_pile[-1]

    if request.method == "POST":
        action = request.form["action"]
        if action == "play":
            card_index = int(request.form["card_index"])
            selected_card = player_hand[card_index]
            if game_manager.is_valid_play(selected_card):
                game_manager.play_card(selected_card)
            else:
                return render_template(
                    "game.html",
                    player=current_player + 1,
                    hand=player_hand,
                    top_card=top_card,
                    error="Invalid card selected!"
                )
        elif action == "draw":
            game_manager.draw_card()

        winner = game_manager.check_winner()
        if winner is not None:
            return redirect(url_for("winner", winner=winner + 1))

        game_manager.next_turn()
    
    return render_template("game.html", player=current_player + 1, hand=player_hand, top_card=top_card)

@app.route("/winner")
def winner():
    winner = request.args.get("winner")
    return render_template("winner.html", winner=winner)

if __name__ == "__main__":
    app.run(debug=True)
