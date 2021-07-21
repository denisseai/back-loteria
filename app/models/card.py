from app import db

class Card (db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String)
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.deck_id'), nullable = False)