from app import db

class Player (db.Model):
    player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    game_players = db.relationship('GamePlayer', backref='player', lazy=True)