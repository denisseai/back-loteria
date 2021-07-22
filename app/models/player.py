from app import db

class Player (db.Model):
    player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    win_count = db.Column(db.Integer, default=0)