from werkzeug.exceptions import BadRequest

from models import Deck


class DeckManager:
    # returns all decks in db
    @staticmethod
    def get_all():
        return Deck.query.filter_by().all()

    # returns one deck from db
    @staticmethod
    def get_one(id_):
        deck = Deck.query.filter_by(id=id_).first()
        if not deck:
            return BadRequest("Deck with this id doesn't exist")
        return deck
