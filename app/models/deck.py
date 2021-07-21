from app import db

class Deck (db.Model):
    deck_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cards = db.relationship('Card', backref='deck', lazy=True)
    games = db.relationship('Game', backref='deck', lazy=True)
