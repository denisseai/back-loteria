from app import db

class GamePlayer (db.Model):
    game_player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    win_count = db.Column(db.Integer, default=0)
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable = False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'), nullable = False)