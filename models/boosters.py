from db import db


class Booster(db.Model):
    __tablename__ = 'boosters'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'), nullable=False)
    deck = db.relationship('Deck')
