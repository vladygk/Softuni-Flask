from flask_restful import Resource

from managers.decks import DeckManager
from schemas.response_schemas.decks import DeckResponseSchema


class DecksResource(Resource):
    @staticmethod
    def get():
        decks = DeckManager.get_all()

        return DeckResponseSchema(many=True).dump(decks)


class DeckResource(Resource):
    @staticmethod
    def get(id_):
        deck = DeckManager.get_one(id_)

        return DeckResponseSchema().dump(deck)
