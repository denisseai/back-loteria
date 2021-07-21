from app import db

class Game (db.Model):
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_players = db.relationship('GamePlayer', backref='game', lazy=True)
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.deck_id'), nullable = False)