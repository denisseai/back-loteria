from flask import Blueprint, request, jsonify, make_response
from app import db
from dotenv import load_dotenv
from app.models.card import Card
from app.models.deck import Deck

load_dotenv()

decks_bp = Blueprint('decks', __name__, url_prefix='/decks')
@decks_bp.route("/<deck_id>/cards", methods=["GET"])
def handle_cards(deck_id):
    deck = Deck.query.get(deck_id)

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

