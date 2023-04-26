from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.cards import CardManager
from schemas.request_schemas.cards import CardRequestSchema
from schemas.response_schemas.cards import CardResponseSchema
from utils.decorators import validate_schema


class CardsResource(Resource):

    @auth.login_required
    def get(self):
        role = auth.current_user().role.value
        cards = None
        if role == 'admin':
            cards = CardManager.get_all_for_admin()
        elif role == 'user':
            cards = CardManager.get_all_for_user()

        return CardResponseSchema(many=True).dump(cards)

    @auth.login_required
    @validate_schema(CardRequestSchema)
    def post(self):

        data = request.get_json()
        card = CardManager.create_card(data)
        return CardResponseSchema().dump(card), 201


class CardResource(Resource):
    @auth.login_required
    def get(self, id_):
        role = auth.current_user().role.value
        card = None
        if role == 'admin':
            card = CardManager.get_one_for_admin(id_)
        elif role == 'user':
            card = CardManager.get_one_for_user(id_)

        return CardResponseSchema().dump(card)


    @auth.login_required
    @validate_schema(CardRequestSchema)
    def put(self, id_):
        data = request.get_json()
        role = auth.current_user().role.value
        card = None
        if role == 'admin':
            card = CardManager.edit_card_for_admin(data, id_)

        elif role == 'user':
            card = CardManager.edit_card_for_user(data, id_)

        return CardResponseSchema().dump(card)

    @auth.login_required
    def delete(self, id_):
        role = auth.current_user().role.value
        card = None
        if role == 'admin':
            card = CardManager.delete_card_for_admin( id_)

        elif role == 'user':
            card = CardManager.delete_card_for_user( id_)

        return CardResponseSchema().dump(card)
