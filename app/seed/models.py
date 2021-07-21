from app import db
from app.models.card import Card
from app.models.deck import Deck

import csv

def seed():
    the_deck = Deck()
    db.session.add(the_deck)
    db.session.commit()
    with open("data/cards.csv") as csvfile:
        cards = csv.DictReader(csvfile)
        for row in cards:
            record = Card(title=row['title'], url=row['url'], deck_id=the_deck.deck_id)
            db.session.add(record)
        db.session.commit()