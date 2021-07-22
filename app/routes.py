from flask import Blueprint, json, request, jsonify
from app import db
from dotenv import load_dotenv
from app.models.card import Card
from app.models.deck import Deck
from app.models.player import Player
from app.models.game_player import GamePlayer

load_dotenv()

decks_bp = Blueprint('decks', __name__, url_prefix='/decks')
players_bp = Blueprint('players', __name__, url_prefix='/players')
game_player_bp = Blueprint('game_player', __name__, url_prefix='/game_player')

@game_player_bp.route("/<player_id>", methods=["PATCH"])
def handle_game_player(player_id):
    winner = GamePlayer.query.get_or_404(player_id)
    winner.win_count += 1
    db.session.add(winner)
    db.session.commit()
    return jsonify(winner), 201

@decks_bp.route("/<deck_id>/cards", methods=["GET"])
def handle_cards(deck_id):
    deck = Deck.query.get_or_404(deck_id)

    if request.method == "GET":
        cards = deck.cards
        cards_response = []
        for card in cards:
            cards_response.append({
            "card_id": card.card_id,
            "title": card.title,
            "url": card.url
        })
    return jsonify(cards_response)

@players_bp.route("", methods=["GET", "POST"])
def handle_players():

    if request.method == "GET":
        players = Player.query.all()

        players_response = []
        for player in players:
            players_response.append({
            "player_id": player.player_id,
            "name": player.name
        })
        return jsonify(players_response)

    elif request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body:
            return jsonify({"details": "Missing player name"}), 400
        new_player = Player(name=request_body["name"])
        db.session.add(new_player)
        db.session.commit()
        commited_player = {"player":{"name": new_player.name}}
        return jsonify(commited_player), 201




