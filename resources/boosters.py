from flask_restful import Resource

from managers.boosters import BoosterManager
from schemas.response_schemas.boosters import BoosterResponseSchema


class BoostersResource(Resource):
    @staticmethod
    def get():
        boosters = BoosterManager.get_all()

        return BoosterResponseSchema(many=True).dump(boosters)


class BoostersResourceFiltered(Resource):
    @staticmethod
    def get(deck_name):
        boosters = BoosterManager.get_filtered(deck_name)

        return BoosterResponseSchema(many=True).dump(boosters)
